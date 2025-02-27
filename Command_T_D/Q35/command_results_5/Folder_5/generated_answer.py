import re

def remove_repeat_chars(s):
    return re.sub('(.)\x01(.)\x02(.)\x03(.)\x04(.)\x05(.)\x06(.)\x07(.)\\8', '\x01\x02\x03\x04\x05\x06\x07\\8', s)