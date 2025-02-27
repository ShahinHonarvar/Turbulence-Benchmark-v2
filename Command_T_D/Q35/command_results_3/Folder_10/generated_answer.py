import re

def remove_repeat_chars(str):
    return re.sub('((?:[a-z])\x01+)', '\x01', str[36:-54])