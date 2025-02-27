import re

def remove_repeat_chars(s):
    return re.sub('(\\d+)(\\D)(\\d+)', '\x01\x02\x03', s[103:-1])