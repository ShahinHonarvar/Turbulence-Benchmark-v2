from math import gcd

def gcf_three_nums(lst):
    a = lst[17]
    b = lst[88]
    c = lst[35]
    gcf_ab = gcd(a, b)
    gcf = gcd(gcf_ab, c)
    return gcf