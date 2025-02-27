import math

def gcf_two_nums(lst):
    if len(lst) < 753:
        return None
    return math.gcd(lst[372], lst[752])