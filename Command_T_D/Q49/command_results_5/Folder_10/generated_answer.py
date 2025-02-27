import re

def if_decimal_is_divisible(s):
    return bool(re.fullmatch('0*(10+)+0*', s))