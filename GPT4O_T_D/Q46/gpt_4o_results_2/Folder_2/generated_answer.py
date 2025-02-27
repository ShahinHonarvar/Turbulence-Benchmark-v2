import math

def gcf_three_nums(lst):
    if len(lst) < 921:
        return None
    return math.gcd(math.gcd(lst[307], lst[920]), lst[463])