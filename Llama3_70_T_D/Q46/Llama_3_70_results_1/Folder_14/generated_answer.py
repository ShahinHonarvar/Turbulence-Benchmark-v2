import math

def gcf_three_nums(lst):
    a = lst[17]
    b = lst[88]
    c = lst[35]
    ab_gcf = math.gcd(a, b)
    return math.gcd(ab_gcf, c)