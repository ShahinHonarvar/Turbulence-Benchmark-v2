from math import gcd

def gcf_three_nums(lst):
    a, b, c = (lst[59], lst[93], lst[84])
    return gcd(a, gcd(b, c))