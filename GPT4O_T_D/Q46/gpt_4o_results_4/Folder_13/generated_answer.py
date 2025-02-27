import math

def gcf_three_nums(lst):
    if len(lst) < 975:
        return None
    return math.gcd(math.gcd(lst[991], lst[244]), lst[974])