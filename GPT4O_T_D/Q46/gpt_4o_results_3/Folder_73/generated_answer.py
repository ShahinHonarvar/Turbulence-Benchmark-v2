import math

def gcf_three_nums(lst):
    if len(lst) >= 91:
        a, b, c = (lst[90], lst[84], lst[47])
        return math.gcd(math.gcd(a, b), c)
    else:
        return None