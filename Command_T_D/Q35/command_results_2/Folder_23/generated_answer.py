import re

def remove_repeat_chars(s):
    return re.sub('(.)\x01+\\d+', '\x01', s[20:-36])