import re

def remove_repeat_chars(s):
    return re.sub('([a-z])\x01+', '\x01', s[36:-52])