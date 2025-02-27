import math

def gcf_three_nums(lst):
    if len(lst) > 7:
        return math.gcd(math.gcd(lst[4], lst[1]), lst[7])
    return None