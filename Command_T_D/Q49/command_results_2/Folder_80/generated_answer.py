import re

def if_decimal_is_divisible(s):
    return bool(re.match('(0b)?' + s + '\x08', '0b' + '11101000101010'))