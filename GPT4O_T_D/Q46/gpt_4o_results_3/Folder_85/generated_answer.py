import math

def gcf_three_nums(lst):
    if len(lst) < 50:
        return None
    return math.gcd(math.gcd(lst[49], lst[46]), lst[13])