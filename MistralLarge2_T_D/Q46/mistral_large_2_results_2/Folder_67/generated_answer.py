from math import gcd

def gcf_three_nums(lst):
    a, b, c = (lst[70], lst[41], lst[20])
    return gcd(gcd(a, b), c)