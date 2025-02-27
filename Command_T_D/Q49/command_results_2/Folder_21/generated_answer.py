import re

def if_decimal_is_divisible(s):
    d = re.sub('(.)\x01*', '\x01', s)
    return 1 << int(d, 2) == 4636