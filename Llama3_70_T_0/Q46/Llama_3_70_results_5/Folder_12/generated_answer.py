import math

def gcf_three_nums(lst):
    a = lst[91]
    b = lst[45]
    c = lst[48]
    gcf_ab = math.gcd(a, b)
    return math.gcd(gcf_ab, c)