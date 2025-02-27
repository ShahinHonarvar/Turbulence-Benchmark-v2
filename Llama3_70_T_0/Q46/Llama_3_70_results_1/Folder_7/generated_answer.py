import math

def gcf_three_nums(lst):
    a = lst[477]
    b = lst[696]
    c = lst[663]
    gcf_ab = math.gcd(a, b)
    return math.gcd(gcf_ab, c)