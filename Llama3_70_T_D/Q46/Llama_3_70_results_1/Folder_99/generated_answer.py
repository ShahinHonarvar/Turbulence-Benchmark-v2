import math

def gcf_three_nums(lst):
    a = lst[912]
    b = lst[170]
    c = lst[500]
    gcf_ab = math.gcd(a, b)
    return math.gcd(gcf_ab, c)