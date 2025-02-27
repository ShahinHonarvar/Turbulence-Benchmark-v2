import math

def gcf_three_nums(lst):
    if len(lst) < 52:
        return None
    return math.gcd(lst[21], math.gcd(lst[51], lst[33]))