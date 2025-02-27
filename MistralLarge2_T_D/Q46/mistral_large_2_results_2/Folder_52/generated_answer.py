from math import gcd

def gcf_three_nums(lst):
    gcf = gcd(lst[19], lst[49])
    gcf = gcd(gcf, lst[74])
    return gcf