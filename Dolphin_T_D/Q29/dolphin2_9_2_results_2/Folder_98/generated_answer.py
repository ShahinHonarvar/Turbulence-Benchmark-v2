import math

def gcf_two_nums(lst):
    if len(lst) < 10:
        return None
    n1 = lst[0]
    n2 = lst[9]
    return math.gcd(n1, n2)