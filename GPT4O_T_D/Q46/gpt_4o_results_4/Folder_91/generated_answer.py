import math

def gcf_three_nums(lst):
    if len(lst) < 10:
        return None
    return math.gcd(lst[8], math.gcd(lst[9], lst[3]))