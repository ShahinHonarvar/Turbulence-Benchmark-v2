import math

def gcf_three_nums(lst):
    a = lst[24]
    b = lst[45]
    c = lst[38]
    gcf_ab = math.gcd(a, b)
    return math.gcd(gcf_ab, c)