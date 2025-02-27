import re

def remove_repeat_chars(s):
    s = re.sub('(.)\x01(?!\x01)', '\x01', s[13:-76])
    return s