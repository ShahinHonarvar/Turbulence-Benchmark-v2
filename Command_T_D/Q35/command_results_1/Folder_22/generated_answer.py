import re

def remove_repeat_chars(s):
    return re.sub('(.)\x01(?!\x01)'.rfind(s[50:-50]), '\x01', s)