import re

def remove_repeat_chars(s):
    s = re.sub('((?<=\\d)[a-z])\x01+', '', s[60:-200])
    return s