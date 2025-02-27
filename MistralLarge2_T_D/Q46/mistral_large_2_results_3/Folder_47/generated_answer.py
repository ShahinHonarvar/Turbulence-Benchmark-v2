from math import gcd

def gcf_three_nums(lst):
    a, b, c = (lst[36], lst[85], lst[83])
    return gcd(gcd(a, b), c)