import telebot
import requests
import json


bot = telebot.TeleBot('6860414089:AAHw2L9ifHBZDK9_Tv4A63RWtNzZ8odQTCc')

API = 'cb60998de921df3c34a91af207821fa8'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Добро пожаловать! Данный бот предсказывает погоду именно в твоем городе🥰. Введи название города!')




@bot.message_handler(content_types=['text'])
def get_weather(message):
    def name_weather(weather_name):
        if weather_name == 'light snow':
            weather_name_name = 'легкий снег'
        elif weather_name == 'broken clouds':
            weather_name_name = 'большая облачность'
        elif weather_name == 'few clouds':
            weather_name_name = 'уменьшенная облачность'
        elif weather_name == 'clear sky':
            weather_name_name = 'чистое небо'
        elif weather_name == 'light rain':
            weather_name_name = 'легкий дождь'
        elif weather_name == 'overcast clouds':
            weather_name_name = 'пасмурные облака'
        elif weather_name == 'overcast clouds':
            weather_name_name = 'пасмурные облака'
        else:
            weather_name_name = 'погода странная'

        return weather_name_name


    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        count = 0
        count1 = 0
        count2 = 0
        while count2 != 5:
            print(data['list'][count]['weather'][0]['description'])
            time_city = data['list'][count]['dt_txt']

            time_time1 = data['list'][count]['dt_txt']

            if time_time1[11:16] == '03:00' and count1 == 0:
                count1 = 1
                time_time1 = data['list'][count]['dt_txt']
                weather_name1 = data['list'][count]['weather'][0]['description']
                time_time2 = data['list'][count + 2]['dt_txt']
                weather_name2 = data['list'][count+2]['weather'][0]['description']
                time_time3 = data['list'][count + 3]['dt_txt']
                weather_name3 = data['list'][count+3]['weather'][0]['description']
                time_time4 = data['list'][count + 5]['dt_txt']
                weather_name4 = data['list'][count+5]['weather'][0]['description']
                time_time5 = data['list'][count + 6]['dt_txt']
                weather_name5 = data['list'][count+6]['weather'][0]['description']
                temp_city_1 = round(data['list'][count]['main']['temp'])
                temp_city_2 = round(data['list'][count + 2]['main']['temp'])
                temp_city_3 = round(data['list'][count + 3]['main']['temp'])
                temp_city_4 = round(data['list'][count + 5]['main']['temp'])
                temp_city_5 = round(data['list'][count + 6]['main']['temp'])
                bot.send_message(message.chat.id, f'{time_city[:11]} в {city}\n'
                                                  f'{time_time1[11:16]}   {temp_city_1}°   {name_weather(weather_name1)}\n'
                                                  f'{time_time2[11:16]}   {temp_city_2}°   {name_weather(weather_name2)}\n'
                                                  f'{time_time3[11:16]}   {temp_city_3}°   {name_weather(weather_name3)}\n'
                                                  f'{time_time4[11:16]}   {temp_city_4}°   {name_weather(weather_name4)}\n'
                                                  f'{time_time5[11:16]}   {temp_city_5}°   {name_weather(weather_name5)}\n')
                count = -1

            elif time_time1[11:16] == '06:00' and count1 == 0:
                count1 = 1
                time_time1 = data['list'][count]['dt_txt']
                weather_name1 = data['list'][count]['weather'][0]['description']
                time_time2 = data['list'][count + 2]['dt_txt']
                weather_name2 = data['list'][count+2]['weather'][0]['description']
                time_time3 = data['list'][count + 4]['dt_txt']
                weather_name3 = data['list'][count+4]['weather'][0]['description']
                time_time4 = data['list'][count + 5]['dt_txt']
                weather_name4 = data['list'][count+5]['weather'][0]['description']
                temp_city_1 = round(data['list'][count]['main']['temp'])
                temp_city_2 = round(data['list'][count + 2]['main']['temp'])
                temp_city_3 = round(data['list'][count + 4]['main']['temp'])
                temp_city_4 = round(data['list'][count + 5]['main']['temp'])
                bot.send_message(message.chat.id, f'{time_city[:11]} в {city}\n'
                                                  f'{time_time1[11:16]}   {temp_city_1}°   {name_weather(weather_name1)}\n'
                                                  f'{time_time2[11:16]}   {temp_city_2}°   {name_weather(weather_name2)}\n'
                                                  f'{time_time3[11:16]}   {temp_city_3}°   {name_weather(weather_name3)}\n'
                                                  f'{time_time4[11:16]}   {temp_city_4}°   {name_weather(weather_name4)}\n')
                count = -2

            elif time_time1[11:16] == '09:00' and count1 == 0:
                count1 = 1
                time_time1 = data['list'][count]['dt_txt']
                weather_name1 = data['list'][count]['weather'][0]['description']
                time_time2 = data['list'][count + 1]['dt_txt']
                weather_name2 = data['list'][count+1]['weather'][0]['description']
                time_time3 = data['list'][count + 3]['dt_txt']
                weather_name3 = data['list'][count+3]['weather'][0]['description']
                time_time4 = data['list'][count + 4]['dt_txt']
                weather_name4 = data['list'][count+4]['weather'][0]['description']
                temp_city_1 = round(data['list'][count]['main']['temp'])
                temp_city_2 = round(data['list'][count + 1]['main']['temp'])
                temp_city_3 = round(data['list'][count + 3]['main']['temp'])
                temp_city_4 = round(data['list'][count + 4]['main']['temp'])
                bot.send_message(message.chat.id, f'{time_city[:11]} в {city}\n'
                                                  f'{time_time1[11:16]}   {temp_city_1}°   {name_weather(weather_name1)}\n'
                                                  f'{time_time2[11:16]}   {temp_city_2}°   {name_weather(weather_name2)}\n'
                                                  f'{time_time3[11:16]}   {temp_city_3}°   {name_weather(weather_name3)}\n'
                                                  f'{time_time4[11:16]}   {temp_city_4}°   {name_weather(weather_name4)}\n')
                count = -3

            elif time_time1[11:16] == '12:00' and count1 == 0:
                count1 = 1
                time_time1 = data['list'][count]['dt_txt']
                weather_name1 = data['list'][count]['weather'][0]['description']
                time_time2 = data['list'][count + 2]['dt_txt']
                weather_name2 = data['list'][count+2]['weather'][0]['description']
                time_time3 = data['list'][count + 3]['dt_txt']
                weather_name3 = data['list'][count+3]['weather'][0]['description']
                temp_city_1 = round(data['list'][count]['main']['temp'])
                temp_city_2 = round(data['list'][count + 2]['main']['temp'])
                temp_city_3 = round(data['list'][count + 3]['main']['temp'])
                bot.send_message(message.chat.id, f'{time_city[:11]} в {city}\n'
                                                  f'{time_time1[11:16]}   {temp_city_1}°   {name_weather(weather_name1)}\n'
                                                  f'{time_time2[11:16]}   {temp_city_2}°   {name_weather(weather_name2)}\n'
                                                  f'{time_time3[11:16]}   {temp_city_3}°   {name_weather(weather_name3)}\n')
                count = -4

            elif time_time1[11:16] == '15:00' and count1 == 0:
                count1 = 1
                time_time1 = data['list'][count]['dt_txt']
                weather_name1 = data['list'][count]['weather'][0]['description']
                time_time2 = data['list'][count + 1]['dt_txt']
                weather_name2 = data['list'][count+1]['weather'][0]['description']
                time_time3 = data['list'][count + 2]['dt_txt']
                weather_name3 = data['list'][count+2]['weather'][0]['description']
                temp_city_1 = round(data['list'][count]['main']['temp'])
                temp_city_2 = round(data['list'][count + 1]['main']['temp'])
                temp_city_3 = round(data['list'][count + 2]['main']['temp'])
                bot.send_message(message.chat.id, f'{time_city[:11]} в {city}\n'
                                                  f'{time_time1[11:16]}   {temp_city_1}°   {name_weather(weather_name1)}\n'
                                                  f'{time_time2[11:16]}   {temp_city_2}°   {name_weather(weather_name2)}\n'
                                                  f'{time_time3[11:16]}   {temp_city_3}°   {name_weather(weather_name3)}\n')
                count = -5

            elif time_time1[11:16] == '18:00' and count1 == 0:
                count1 = 1
                time_time1 = data['list'][count]['dt_txt']
                weather_name1 = data['list'][count]['weather'][0]['description']
                time_time2 = data['list'][count + 1]['dt_txt']
                weather_name2 = data['list'][count+1]['weather'][0]['description']
                temp_city_1 = round(data['list'][count]['main']['temp'])
                temp_city_2 = round(data['list'][count + 1]['main']['temp'])
                bot.send_message(message.chat.id, f'{time_city[:11]} в {city}\n'
                                                  f'{time_time1[11:16]}   {temp_city_1}°   {name_weather(weather_name1)}\n'
                                                  f'{time_time2[11:16]}   {temp_city_2}°   {name_weather(weather_name2)}\n')
                count = -6

            elif time_time1[11:16] == '21:00' and count1 == 0:
                count1 = 1
                time_time1 = data['list'][count]['dt_txt']
                weather_name1 = data['list'][count]['weather'][0]['description']
                temp_city_1 = round(data['list'][count]['main']['temp'])
                bot.send_message(message.chat.id, f'{time_city[:11]} в {city}\n'
                                                  f'{time_time1[11:16]}   {temp_city_1}°   {name_weather(weather_name1)}\n')
                count = -7


            else:
                time_time1 = data['list'][count]['dt_txt']
                weather_name1 = data['list'][count]['weather'][0]['description']
                time_time2 = data['list'][count + 2]['dt_txt']
                weather_name2 = data['list'][count+2]['weather'][0]['description']
                time_time3 = data['list'][count + 4]['dt_txt']
                weather_name3 = data['list'][count+4]['weather'][0]['description']
                time_time4 = data['list'][count + 6]['dt_txt']
                weather_name4 = data['list'][count+6]['weather'][0]['description']
                time_time5 = data['list'][count + 7]['dt_txt']
                weather_name5 = data['list'][count+7]['weather'][0]['description']

                temp_city_1 = round(data['list'][count]['main']['temp'])
                temp_city_2 = round(data['list'][count + 2]['main']['temp'])
                temp_city_3 = round(data['list'][count + 4]['main']['temp'])
                temp_city_4 = round(data['list'][count + 6]['main']['temp'])
                temp_city_5 = round(data['list'][count + 7]['main']['temp'])
                bot.send_message(message.chat.id, f'{time_city[:11]} в {city}\n'
                                                  f'{time_time1[11:16]}   {temp_city_1}°   {name_weather(weather_name1)}\n'
                                                  f'{time_time2[11:16]}   {temp_city_2}°   {name_weather(weather_name2)}\n'
                                                  f'{time_time3[11:16]}   {temp_city_3}°   {name_weather(weather_name3)}\n'
                                                  f'{time_time4[11:16]}   {temp_city_4}°   {name_weather(weather_name4)}\n'
                                                  f'{time_time5[11:16]}   {temp_city_5}°   {name_weather(weather_name5)}\n')

            count2 +=1
            count += 8


    else:
        bot.send_message(message.chat.id, 'Я не знаю этот город!!!')

bot.polling(none_stop=True)