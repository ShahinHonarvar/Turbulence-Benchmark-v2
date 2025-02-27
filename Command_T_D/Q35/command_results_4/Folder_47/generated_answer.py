import re

def remove_repeat_chars(text):
    return re.sub('((?<=\\d)[a-z])\x01+(?=\\d)', '', text)