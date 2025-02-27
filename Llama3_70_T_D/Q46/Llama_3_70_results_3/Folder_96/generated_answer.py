import math

def gcf_three_nums(lst):
    a = lst[29]
    b = lst[74]
    c = lst[49]
    gcf_ab = math.gcd(a, b)
    return math.gcd(gcf_ab, c)