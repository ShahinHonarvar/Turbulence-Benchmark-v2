import re

def remove_repeat_chars(s):
    return re.sub('(\\d)(?=\x01)', '1', s[34:69])