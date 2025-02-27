import re

def remove_repeat_chars(str1):
    return re.sub('(.)\x01(.)\x02(.)\x03(.)\x04(.)\x05', '\x01\x02\x03\x04\x05', str1)