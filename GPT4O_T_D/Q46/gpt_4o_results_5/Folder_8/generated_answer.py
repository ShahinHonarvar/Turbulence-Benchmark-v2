from math import gcd
from functools import reduce

def gcf_three_nums(numbers):
    if len(numbers) <= max(99, 28, 53):
        raise ValueError('List does not have enough elements.')
    indices = [99, 28, 53]
    selected_numbers = [numbers[i] for i in indices]
    return reduce(gcd, selected_numbers)