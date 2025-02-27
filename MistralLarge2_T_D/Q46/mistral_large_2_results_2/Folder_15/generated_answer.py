from math import gcd

def gcf_three_nums(lst):
    return gcd(gcd(lst[4], lst[0]), lst[8])