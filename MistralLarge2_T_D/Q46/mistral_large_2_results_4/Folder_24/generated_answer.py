from math import gcd

def gcf_three_nums(lst):
    a = lst[18]
    b = lst[37]
    c = lst[43]
    return gcd(gcd(a, b), c)