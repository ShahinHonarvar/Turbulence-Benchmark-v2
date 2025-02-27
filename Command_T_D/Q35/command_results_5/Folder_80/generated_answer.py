import re

def remove_repeat_chars(s):
    return re.sub('(.)\x01+', '\x01', s[57:-84])