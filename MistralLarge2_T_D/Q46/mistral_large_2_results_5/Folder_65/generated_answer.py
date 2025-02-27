from math import gcd

def gcf_three_nums(lst):
    gcf = gcd(lst[18], lst[10])
    gcf = gcd(gcf, lst[76])
    return gcf