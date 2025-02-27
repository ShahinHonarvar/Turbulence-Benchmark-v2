from math import gcd

def gcf_three_nums(lst: list) -> int:
    a = lst[70]
    b = lst[98]
    c = lst[22]
    l = gcd(a, b)
    l = gcd(l, c)
    return l