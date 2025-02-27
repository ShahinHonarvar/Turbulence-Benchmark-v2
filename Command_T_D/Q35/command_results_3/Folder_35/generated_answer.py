import re

def remove_repeat_chars(s):
    s = re.sub('(.)\x01+', '\x01', s[77:-84])
    return s