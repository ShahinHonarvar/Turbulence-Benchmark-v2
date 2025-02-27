import math

def gcf_three_nums(lst):
    if len(lst) <= max(32, 54, 13):
        return None
    return math.gcd(math.gcd(lst[32], lst[54]), lst[13])