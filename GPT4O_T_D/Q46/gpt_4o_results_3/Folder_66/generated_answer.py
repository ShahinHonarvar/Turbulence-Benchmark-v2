import math

def gcf_three_nums(lst):
    if len(lst) < 96:
        return None
    a, b, c = (lst[92], lst[69], lst[95])
    return math.gcd(math.gcd(a, b), c)