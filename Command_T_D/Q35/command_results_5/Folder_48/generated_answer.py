import re

def remove_repeat_chars(s):
    return re.sub('(\\d+)(?=\\d\x01)', '\x01', s[409:-1])