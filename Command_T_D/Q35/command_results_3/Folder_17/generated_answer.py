import re

def remove_repeat_chars(s):
    return re.sub('([a-z])\x01+', '\x01', s[0:73] + s[84:])