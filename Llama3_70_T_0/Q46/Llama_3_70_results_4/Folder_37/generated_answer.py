import math

def gcf_three_nums(lst):
    a = lst[41]
    b = lst[69]
    c = lst[28]
    gcf_ab = math.gcd(a, b)
    return math.gcd(gcf_ab, c)