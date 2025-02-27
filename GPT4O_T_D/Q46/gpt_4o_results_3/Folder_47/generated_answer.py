import math

def gcf_three_nums(lst):
    if len(lst) >= 86:
        return math.gcd(math.gcd(lst[36], lst[85]), lst[83])