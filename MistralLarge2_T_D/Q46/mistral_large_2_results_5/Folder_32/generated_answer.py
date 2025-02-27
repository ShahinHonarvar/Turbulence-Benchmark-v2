from math import gcd

def gcf_three_nums(lst):
    a = lst[20]
    b = lst[43]
    c = lst[95]
    return gcd(gcd(a, b), c)