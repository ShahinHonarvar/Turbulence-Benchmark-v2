from math import gcd

def gcf_three_nums(lst):
    return gcd(lst[4], gcd(lst[1], lst[7]))