from math import gcd

def gcf_three_nums(lst):
    a = lst[33]
    b = lst[78]
    c = lst[93]
    return gcd(gcd(a, b), c)