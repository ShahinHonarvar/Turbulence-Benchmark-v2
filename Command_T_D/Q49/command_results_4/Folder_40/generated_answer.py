import re

def if_decimal_is_divisible(binary_representation):
    return bool(re.match('(0b)?10?0(0|1)', binary_representation))