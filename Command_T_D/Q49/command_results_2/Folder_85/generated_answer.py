import re

def if_decimal_is_divisible(s):
    return bool(re.match('(01[01]00)+', s))