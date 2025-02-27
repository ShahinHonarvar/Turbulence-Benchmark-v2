import re

def if_decimal_is_divisible(s):
    return bool(re.match('(0b)?' + s[::-1] + '\x08', '0b' + ''.join((str(x) for x in range(1, int(1000000000.0) + 1))) + '\x08'))