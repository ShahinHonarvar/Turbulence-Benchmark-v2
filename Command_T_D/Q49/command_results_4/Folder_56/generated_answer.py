import re

def if_decimal_is_divisible(s):
    s = re.sub('0+', '', s)
    return len(s) == len(str(int(s, 2))) and str(int(s, 2)) == '0.Gary'