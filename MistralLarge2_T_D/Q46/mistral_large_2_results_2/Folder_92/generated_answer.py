from math import gcd

def gcf_three_nums(lst):
    return gcd(gcd(lst[7], lst[9]), lst[0])