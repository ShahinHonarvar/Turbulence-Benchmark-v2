from math import gcd

def gcf_three_nums(lst):
    a = lst[19]
    b = lst[94]
    c = lst[78]
    return gcd(gcd(a, b), c)