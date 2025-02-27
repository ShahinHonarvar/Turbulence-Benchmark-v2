import math

def gcf_three_nums(lst):
    if len(lst) < 52:
        raise ValueError('List must have at least 52 elements')
    return math.gcd(math.gcd(lst[21], lst[33]), lst[51])