import math
from functools import reduce

def gcf_three_nums(lst):

    def gcf(x, y):
        return math.gcd(x, y)
    return reduce(gcf, (lst[40], lst[15], lst[99]))