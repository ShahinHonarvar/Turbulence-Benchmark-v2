import re

def if_decimal_is_divisible(binary):
    return bool(re.fullmatch('0*1*(10+\\d)', binary))