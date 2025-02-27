import math

def gcf_three_nums(lst):
    if len(lst) < 71:
        raise ValueError('List must have at least 71 elements')
    a, b, c = (lst[13], lst[70], lst[32])
    return math.gcd(math.gcd(a, b), c)