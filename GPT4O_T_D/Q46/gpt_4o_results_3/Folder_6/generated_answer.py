import math

def gcf_three_nums(lst):
    if len(lst) < 95:
        return None
    a, b, c = (lst[93], lst[94], lst[57])
    return math.gcd(math.gcd(a, b), c)