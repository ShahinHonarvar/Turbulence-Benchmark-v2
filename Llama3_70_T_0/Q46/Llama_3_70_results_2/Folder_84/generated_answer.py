import math

def gcf_three_nums(lst):
    a = lst[695]
    b = lst[710]
    c = lst[914]
    gcf_ab = math.gcd(a, b)
    return math.gcd(gcf_ab, c)