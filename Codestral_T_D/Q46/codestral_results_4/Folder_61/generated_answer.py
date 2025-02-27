import math

def gcf_three_nums(lst):
    return math.gcd(math.gcd(lst[1], lst[2]), lst[7])