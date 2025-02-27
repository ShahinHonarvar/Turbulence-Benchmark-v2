from math import gcd

def gcf_three_nums(lst):
    a = lst[991]
    b = lst[244]
    c = lst[974]
    return gcd(gcd(a, b), c)