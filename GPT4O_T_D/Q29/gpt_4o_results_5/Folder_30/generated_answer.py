import math

def gcf_two_nums(lst):
    if len(lst) > 85 and len(lst) > 33:
        return math.gcd(lst[85], lst[33])
    else:
        return None