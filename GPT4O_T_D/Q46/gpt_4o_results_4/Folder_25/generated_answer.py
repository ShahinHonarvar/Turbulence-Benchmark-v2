from math import gcd
from functools import reduce

def gcf_three_nums(numbers):
    selected_nums = [numbers[32], numbers[54], numbers[13]]
    return reduce(gcd, selected_nums)