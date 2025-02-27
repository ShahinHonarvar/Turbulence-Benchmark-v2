import math

def gcf_three_nums(lst):
    a = lst[9]
    b = lst[6]
    c = lst[2]
    ab_gcf = math.gcd(a, b)
    return math.gcd(ab_gcf, c)