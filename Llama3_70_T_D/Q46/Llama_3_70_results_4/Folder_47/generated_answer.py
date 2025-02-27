import math

def gcf_three_nums(lst):
    a = lst[36]
    b = lst[85]
    c = lst[83]
    gcf_ab = math.gcd(a, b)
    return math.gcd(gcf_ab, c)