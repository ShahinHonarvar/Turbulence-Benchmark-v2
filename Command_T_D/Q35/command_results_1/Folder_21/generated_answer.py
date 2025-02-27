import re

def remove_repeat_chars(s):
    return re.sub('(\\w)\x01+\x08(?!\x01)', '\x01', s[462:-3])