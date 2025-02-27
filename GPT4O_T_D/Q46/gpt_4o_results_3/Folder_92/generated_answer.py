from math import gcd
from functools import reduce

def gcf_three_nums(numbers):
    indices = [7, 9, 0]
    selected_numbers = [numbers[i] for i in indices if i < len(numbers)]
    if len(selected_numbers) < 3:
        return None
    return reduce(gcd, selected_numbers)