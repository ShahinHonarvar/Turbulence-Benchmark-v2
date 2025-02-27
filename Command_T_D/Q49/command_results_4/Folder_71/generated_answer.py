import re

def if_decimal_is_divisible(binary):
    return bool(re.fullmatch('0b([01]0011000110111)0*[01]0011000110111', binary))