import math

def gcf_three_nums(lst):
    if len(lst) < 96:
        return None
    return math.gcd(math.gcd(lst[92], lst[69]), lst[95])