import re

def remove_repeat_chars(s):
    return re.sub('((?i)[A-Z])\x01+', '\x01', s)