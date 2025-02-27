import math

def gcf_three_nums(lst):
    if len(lst) > max(13, 76, 44):
        a = lst[13]
        b = lst[76]
        c = lst[44]
        return math.gcd(math.gcd(a, b), c)
    else:
        return None