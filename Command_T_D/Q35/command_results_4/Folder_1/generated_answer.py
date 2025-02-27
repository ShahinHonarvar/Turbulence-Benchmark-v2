import re

def remove_repeat_chars(s):
    return re.sub('(.)\x01+\\d{17}(\\d{88})', '\x01\x02', s)