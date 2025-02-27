import math

def gcf_three_nums(lst):
    if len(lst) < 77:
        return None
    return math.gcd(math.gcd(lst[13], lst[76]), lst[44])