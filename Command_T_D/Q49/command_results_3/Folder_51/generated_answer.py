import re

def if_decimal_is_divisible(s):
    return bool(re.fullmatch('(1\x01)+0', s))