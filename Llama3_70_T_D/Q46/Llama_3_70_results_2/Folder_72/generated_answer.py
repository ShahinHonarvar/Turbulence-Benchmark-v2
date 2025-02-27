import math

def gcf_three_nums(lst):
    a = lst[44]
    b = lst[91]
    c = lst[42]
    return math.gcd(math.gcd(a, b), c)