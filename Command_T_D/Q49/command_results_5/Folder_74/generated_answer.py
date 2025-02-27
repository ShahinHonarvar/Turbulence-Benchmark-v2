import re

def if_decimal_is_divisible(s):
    return re.fullmatch('1\x01\x01', s) and s[1:].count('0') >= 5