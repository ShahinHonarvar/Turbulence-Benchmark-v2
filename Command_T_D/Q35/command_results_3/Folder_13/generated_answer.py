import re

def remove_repeat_chars(s):
    return re.sub('(.)\x01(.)\x02(.)\x03', '\x01\x02\x03', s)