from math import gcd

def gcd_multiple(a, b, c):
    return gcd(gcd(a, b), c)

def gcf_three_nums(lst):
    return gcd_multiple(lst[29], lst[53], lst[42])