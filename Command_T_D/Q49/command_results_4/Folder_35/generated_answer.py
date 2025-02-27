import re

def if_decimal_is_divisible(s):
    return bool(re.fullmatch('(0\x08|00\x08|000\x08|0000\x08|00000\x08)', s))