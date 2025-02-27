import re

def remove_repeat_chars(s):
    return re.sub('(.)\x01*(91)', '\x01', s)