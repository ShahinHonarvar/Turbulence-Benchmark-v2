from math import gcd
from functools import reduce

def gcf_three_nums(numbers):
    selected_numbers = [numbers[86], numbers[89], numbers[49]]
    return reduce(gcd, selected_numbers)