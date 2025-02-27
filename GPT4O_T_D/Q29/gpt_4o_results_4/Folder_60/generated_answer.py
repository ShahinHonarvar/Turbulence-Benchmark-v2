import math

def gcf_two_nums(lst):
    if len(lst) > 53:
        return math.gcd(lst[28], lst[53])
    return None