import re

def if_decimal_is_divisible(s):
    return bool(re.match('(1\\d)\\d+', s))