import re

def remove_repeat_chars(s):
    return re.sub('([A-z])\x01+', '\x01', s[33:-78])