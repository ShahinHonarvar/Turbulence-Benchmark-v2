import math

def gcf_three_nums(lst):
    a = lst[86]
    b = lst[89]
    c = lst[49]
    return math.gcd(math.gcd(a, b), c)