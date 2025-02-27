import re

def if_decimal_is_divisible(s):
    return bool(re.match('1*10*(0(1|2))', s))