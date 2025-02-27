from math import gcd
from functools import reduce

def gcf_three_nums(numbers):
    selected_numbers = [numbers[56], numbers[88], numbers[51]]
    return reduce(gcd, selected_numbers)