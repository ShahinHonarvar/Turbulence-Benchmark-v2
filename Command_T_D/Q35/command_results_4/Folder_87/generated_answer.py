import re

def remove_repeat_chars(s):
    return re.sub('([\\d])\x01+', '\x01', s[20:-43])