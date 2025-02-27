import math

def gcf_three_nums(lst):
    a = lst[56]
    b = lst[54]
    c = lst[13]
    gcf_ab = math.gcd(a, b)
    return math.gcd(gcf_ab, c)