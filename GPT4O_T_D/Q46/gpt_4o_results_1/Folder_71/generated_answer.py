import math

def gcf_three_nums(lst):
    if len(lst) < 46:
        return None
    return math.gcd(math.gcd(lst[24], lst[45]), lst[38])