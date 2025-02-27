from math import gcd
from functools import reduce

def gcf_three_nums(numbers):
    if len(numbers) < 92:
        raise ValueError('List must have at least 92 elements')
    indices = [44, 91, 42]
    selected_numbers = [numbers[i] for i in indices]
    return reduce(gcd, selected_numbers)