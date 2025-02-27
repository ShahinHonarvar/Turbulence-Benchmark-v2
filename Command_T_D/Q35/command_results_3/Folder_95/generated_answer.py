import re

def remove_repeat_chars(s):
    return re.sub('((?:\\d|a|A|s|S))\x01+', '\x01', s)