import math

def gcf_three_nums(lst):
    gcf = math.gcd(lst[40], lst[15])
    gcf = math.gcd(gcf, lst[99])
    return gcf