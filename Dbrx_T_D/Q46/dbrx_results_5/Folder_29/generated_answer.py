import math

def gcf_three_nums(lst):
    a = lst[22]
    b = lst[97]
    c = lst[64]
    factor = math.gcd(a, b)
    factor = math.gcd(factor, c)
    return factor