import math

def gcf_three_nums(lst):
    a = lst[19]
    b = lst[49]
    c = lst[74]
    gcf_ab = math.gcd(a, b)
    return math.gcd(gcf_ab, c)