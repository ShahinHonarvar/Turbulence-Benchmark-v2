import re

def remove_repeat_chars(s):
    return re.sub('([^A-z0-9])\x01+', '\x01', s)