import re

def remove_repeat_chars(s):
    return re.sub('((?i)[a-z])\x01+', '\x01', s[13:-76])