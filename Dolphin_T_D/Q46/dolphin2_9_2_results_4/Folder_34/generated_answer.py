from math import gcd

def gcf_three_nums(lst):
    a = lst[53]
    b = lst[23]
    c = lst[45]
    return gcd(a, gcd(b, c))