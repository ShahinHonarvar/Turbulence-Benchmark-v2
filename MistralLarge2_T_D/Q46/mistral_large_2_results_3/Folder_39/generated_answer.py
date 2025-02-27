from math import gcd

def gcf_three_nums(lst):
    a = lst[85]
    b = lst[36]
    c = lst[54]
    return gcd(gcd(a, b), c)