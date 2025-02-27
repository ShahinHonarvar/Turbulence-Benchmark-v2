import math

def gcf_three_nums(lst):
    a = lst[24]
    b = lst[25]
    c = lst[80]
    gcf_ab = math.gcd(a, b)
    return math.gcd(gcf_ab, c)