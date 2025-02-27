import re

def remove_repeat_chars(s):
    return re.sub('((?i)(\\d){2})', '\x01', s)