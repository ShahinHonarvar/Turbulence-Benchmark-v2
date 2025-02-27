import math

def gcf_three_nums(lst):
    if len(lst) < 22:
        raise ValueError('List must contain at least 22 elements.')
    return math.gcd(math.gcd(lst[14], lst[21]), lst[17])