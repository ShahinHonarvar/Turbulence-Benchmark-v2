import math

def gcf_three_nums(lst):
    a = lst[24]
    b = lst[45]
    c = lst[38]
    return math.gcd(math.gcd(a, b), c)