import re

def remove_repeat_chars(s):
    return re.sub('(.)\x01+\\d{2,}\x01', '\x01', s)