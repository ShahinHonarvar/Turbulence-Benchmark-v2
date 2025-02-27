from math import gcd

def gcf_three_nums(lst):
    if len(lst) >= 835:
        return gcd(gcd(lst[404], lst[834]), lst[517])
    else:
        raise ValueError('List must contain at least 835 elements.')