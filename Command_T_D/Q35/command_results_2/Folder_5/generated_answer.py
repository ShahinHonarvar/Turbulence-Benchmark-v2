import re

def remove_repeat_chars(s):
    return re.sub('([^A-Z0-9])\x01+', '\x01', s[2:-8])