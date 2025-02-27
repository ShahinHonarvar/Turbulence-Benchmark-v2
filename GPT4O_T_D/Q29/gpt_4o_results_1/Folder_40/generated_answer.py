import math

def gcf_two_nums(lst):
    if len(lst) < 10:
        return None
    return math.gcd(lst[7], lst[9])