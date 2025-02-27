import math

def gcf_three_nums(lst):
    a = lst[66]
    b = lst[90]
    c = lst[27]
    gcf_ab = math.gcd(a, b)
    return math.gcd(gcf_ab, c)