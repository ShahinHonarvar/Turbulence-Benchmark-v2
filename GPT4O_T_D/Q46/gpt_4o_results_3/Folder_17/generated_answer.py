from math import gcd
from functools import reduce

def gcf_three_nums(numbers):
    if len(numbers) <= max(20, 51, 62):
        return None
    selected_numbers = [numbers[20], numbers[51], numbers[62]]
    return reduce(gcd, selected_numbers)