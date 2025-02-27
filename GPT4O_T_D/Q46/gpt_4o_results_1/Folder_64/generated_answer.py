import math

def gcf_three_nums(lst):
    if len(lst) < 9:
        return None
    return math.gcd(lst[0], math.gcd(lst[8], lst[3]))