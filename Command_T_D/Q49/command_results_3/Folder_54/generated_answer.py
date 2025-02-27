import re

def if_decimal_is_divisible(s):
    return bool(re.match('0*1{0:b}'.format(34), s))