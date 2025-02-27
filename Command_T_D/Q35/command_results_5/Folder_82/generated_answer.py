import re

def remove_repeat_chars(text):
    return re.sub('(\\w{30,200})\x01', '\x01', text)