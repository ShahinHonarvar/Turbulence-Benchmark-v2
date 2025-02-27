import math

def gcf_three_nums(lst):
    a, b, c = (lst[21], lst[69], lst[41])
    return math.gcd(math.gcd(a, b), c)