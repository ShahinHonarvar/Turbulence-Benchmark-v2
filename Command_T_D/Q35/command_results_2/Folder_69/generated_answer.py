import re

def remove_repeat_chars(text):
    return re.sub('(.)\x01+', '\x01', text[39:-43])