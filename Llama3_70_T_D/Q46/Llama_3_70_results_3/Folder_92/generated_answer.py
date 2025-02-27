import math

def gcf_three_nums(lst):
    a = lst[7]
    b = lst[9]
    c = lst[0]
    return math.gcd(math.gcd(a, b), c)