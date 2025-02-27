import math

def gcf_three_nums(lst):
    a = lst[20]
    b = lst[35]
    c = lst[74]
    gcf_ab = math.gcd(a, b)
    return math.gcd(gcf_ab, c)