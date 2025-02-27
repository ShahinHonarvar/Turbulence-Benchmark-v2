import re

def remove_repeat_chars(s):
    return re.sub('([a-z]{20,36})\x01', '\x01', s)