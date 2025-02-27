import math

def gcf_three_nums(lst):
    a = lst[404]
    b = lst[834]
    c = lst[517]
    gcf_ab = math.gcd(a, b)
    return math.gcd(gcf_ab, c)