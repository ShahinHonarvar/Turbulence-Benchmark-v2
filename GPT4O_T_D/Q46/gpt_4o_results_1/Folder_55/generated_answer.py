from math import gcd
from functools import reduce

def gcf_three_nums(numbers):
    selected_numbers = [numbers[9], numbers[6], numbers[2]]
    return reduce(gcd, selected_numbers)