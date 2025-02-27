import math

def gcf_three_nums(lst):
    a = lst[70]
    b = lst[41]
    c = lst[20]
    gcf_ab = math.gcd(a, b)
    return math.gcd(gcf_ab, c)