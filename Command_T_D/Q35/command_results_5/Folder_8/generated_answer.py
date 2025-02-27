import re

def remove_repeat_chars(s):
    return re.sub('(.)\x01+b', '\x01', s, flags=re.I)