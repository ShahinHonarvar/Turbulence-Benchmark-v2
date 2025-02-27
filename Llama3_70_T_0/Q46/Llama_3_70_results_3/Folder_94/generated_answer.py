import math

def gcf_three_nums(lst):
    a = lst[56]
    b = lst[88]
    c = lst[51]
    gcf_ab = math.gcd(a, b)
    return math.gcd(gcf_ab, c)