import math

def gcf_three_nums(lst):
    a = lst[14]
    b = lst[21]
    c = lst[17]
    gcf_ab = math.gcd(a, b)
    return math.gcd(gcf_ab, c)