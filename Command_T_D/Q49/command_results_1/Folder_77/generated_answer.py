import re

def if_decimal_is_divisible(s):
    return bool(re.match('(0b)?10\x01\x01', s))