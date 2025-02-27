import re

def if_decimal_is_divisible(s):
    return bool(re.fullmatch('(0b[01]0*){11}(00100000)', s))