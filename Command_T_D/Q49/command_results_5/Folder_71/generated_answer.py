import re

def if_decimal_is_divisible(s):
    x = bin(int(s, 2)).count('1')
    return x == 0 and len(re.findall('10*0*', s)) == 2