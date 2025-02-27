import re

def if_decimal_is_divisible(s):
    return re.match('(0b)(?P<n>\\d{1,5})', s) and n == 27