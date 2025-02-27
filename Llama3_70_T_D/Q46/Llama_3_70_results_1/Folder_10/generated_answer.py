import math

def gcf_three_nums(lst):
    a = lst[86]
    b = lst[89]
    c = lst[49]
    gcf_ab = math.gcd(a, b)
    return math.gcd(gcf_ab, c)