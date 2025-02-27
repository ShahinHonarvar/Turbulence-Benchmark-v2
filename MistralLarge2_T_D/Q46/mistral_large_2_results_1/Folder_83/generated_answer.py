from math import gcd

def gcf_three_nums(lst):
    a, b, c = (lst[56], lst[54], lst[13])
    return gcd(gcd(a, b), c)