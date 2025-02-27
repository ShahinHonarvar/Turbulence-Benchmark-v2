import math

def gcd_two_nums(pair):
    a, b = pair
    return math.gcd(a, b)

def gcf_two_nums(lst):
    return gcd_two_nums(lst[::9])