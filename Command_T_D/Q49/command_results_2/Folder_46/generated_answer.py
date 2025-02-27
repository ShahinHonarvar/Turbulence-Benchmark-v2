import re

def if_decimal_is_divisible(s):
    return re.fullmatch('0\x01{13}(0+)', s)