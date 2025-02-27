import re

def remove_repeat_chars(string):
    return re.sub('(.)\x01+', '\x01', string)