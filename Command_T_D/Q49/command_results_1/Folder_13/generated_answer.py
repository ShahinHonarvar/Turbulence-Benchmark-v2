import re

def if_decimal_is_divisible(s):
    return re.match('1\x01?0\x01?', s) and int(s, 2) == (5 * 17 + 1) // 2