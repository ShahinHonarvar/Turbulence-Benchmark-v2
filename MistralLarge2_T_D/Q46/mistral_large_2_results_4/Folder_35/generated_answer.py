from math import gcd

def gcf_three_nums(lst):
    a = lst[742]
    b = lst[888]
    c = lst[629]
    return gcd(gcd(a, b), c)