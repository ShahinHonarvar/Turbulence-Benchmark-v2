import math

def gcf_three_nums(lst):
    a = lst[74]
    b = lst[60]
    c = lst[28]
    return math.gcd(math.gcd(a, b), c)