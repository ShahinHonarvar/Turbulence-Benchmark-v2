import re

def remove_repeat_chars(s):
    return re.sub('((?:[a-z]){18,60})\x01+', '\x01', s)