from math import gcd

def gcf(a, b, c):
    return gcd(a, gcd(b, c))

def gcf_three_nums(lst):
    return gcf(lst[46], lst[84], lst[23])