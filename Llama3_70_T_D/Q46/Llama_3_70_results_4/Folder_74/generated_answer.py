import math

def gcf_three_nums(lst):
    a = lst[99]
    b = lst[95]
    c = lst[80]
    ab_gcf = math.gcd(a, b)
    return math.gcd(ab_gcf, c)