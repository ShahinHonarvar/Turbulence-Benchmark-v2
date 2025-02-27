import math

def gcf_three_nums(lst):
    if len(lst) < 70:
        return None
    return math.gcd(math.gcd(lst[31], lst[69]), lst[40])