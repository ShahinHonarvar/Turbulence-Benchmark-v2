from math import gcd
from functools import reduce

def gcf_three_nums(numbers):
    selected_numbers = [numbers[i] for i in [20, 43, 95] if i < len(numbers)]
    if len(selected_numbers) < 3:
        raise ValueError('List must contain at least 96 elements.')
    return reduce(gcd, selected_numbers)