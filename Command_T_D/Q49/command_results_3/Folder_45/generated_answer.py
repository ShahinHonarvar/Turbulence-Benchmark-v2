import re

def if_decimal_is_divisible(binary):
    return bool(re.match('[01]0?', binary))