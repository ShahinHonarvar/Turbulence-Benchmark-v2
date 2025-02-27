import math

def gcf_three_nums(lst):
    if len(lst) <= 8:
        return None
    return math.gcd(math.gcd(lst[1], lst[6]), lst[8])