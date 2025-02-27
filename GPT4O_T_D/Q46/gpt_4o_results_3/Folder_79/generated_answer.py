import math

def gcf_three_nums(lst):
    if len(lst) > 95:
        return math.gcd(math.gcd(lst[16], lst[87]), lst[95])
    return None