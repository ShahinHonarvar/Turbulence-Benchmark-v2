import math

def gcf_two_nums(lst):
    if len(lst) > 51:
        return math.gcd(lst[51], lst[31])
    return None