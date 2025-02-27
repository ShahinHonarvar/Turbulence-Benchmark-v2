from math import gcd
from functools import reduce

def gcf_three_nums(numbers):
    indices = [27, 85, 51]
    selected_numbers = [numbers[i] for i in indices if i < len(numbers)]
    return reduce(gcd, selected_numbers) if len(selected_numbers) == 3 else None