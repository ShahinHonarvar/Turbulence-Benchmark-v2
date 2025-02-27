from math import gcd

def gcf_two_nums(lst):
    return gcd(lst[3], lst[8]) if len(lst) > 8 else None