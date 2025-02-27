from math import gcd

def gcf_three_nums(lst):
    a = lst[13]
    b = lst[70]
    c = lst[32]
    return gcd(gcd(a, b), c)