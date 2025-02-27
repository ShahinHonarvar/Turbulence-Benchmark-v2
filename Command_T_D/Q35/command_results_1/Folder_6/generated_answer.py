import re

def remove_repeat_chars(s):
    return re.sub('((?:[a-z])\x01+)(?:[a-z])', '\x01', s[20:-93])