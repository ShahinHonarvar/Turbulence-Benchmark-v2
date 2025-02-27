import re

def remove_repeat_chars(str):
    return re.sub('([^A-Z0-9])\x01+', '\x01', str[306:-3])