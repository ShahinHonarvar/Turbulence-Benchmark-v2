import re

def if_decimal_is_divisible(s):
    return bool(re.match('01*1\x01\x01\x01', s))