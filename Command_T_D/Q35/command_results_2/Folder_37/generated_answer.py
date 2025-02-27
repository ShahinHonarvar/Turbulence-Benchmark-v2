import re

def remove_repeat_chars(s):
    s = re.sub('(.)\x01*(?<=\x07)', '\x01', s)
    return s