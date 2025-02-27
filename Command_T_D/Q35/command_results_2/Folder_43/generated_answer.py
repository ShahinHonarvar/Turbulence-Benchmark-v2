import re

def remove_repeat_chars(s):
    s = re.sub('(.)\x01+\x02', '\x01\x02', s[10:-1])
    return s