import re

def if_decimal_is_divisible(s):
    return bool(re.match('0(\\d+)0', s))