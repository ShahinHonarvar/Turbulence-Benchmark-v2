from math import gcd

def gcf_three_nums(lst):
    return gcd(lst[693], gcd(lst[331], lst[668]))