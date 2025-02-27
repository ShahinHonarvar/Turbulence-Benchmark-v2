import re

def remove_repeat_chars(text):
    return re.sub('(.)\x01+\\d+|\\d+\x01+\\d+|\\d+\x01+', '', text)