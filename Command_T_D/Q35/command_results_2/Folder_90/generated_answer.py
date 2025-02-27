import re

def remove_repeat_chars(s):
    return re.sub('((?=.*?[a-zA-Z]))\x01+', '\x01', s[306:-3])