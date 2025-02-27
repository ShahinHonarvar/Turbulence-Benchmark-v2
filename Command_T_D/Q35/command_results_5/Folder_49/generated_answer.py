import re

def remove_repeat_chars(str):
    return re.sub('((?<=90)\x01+(?<=200))', '', str)