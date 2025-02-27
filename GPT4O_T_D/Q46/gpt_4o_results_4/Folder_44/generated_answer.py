from math import gcd
from functools import reduce

def gcf_three_nums(numbers):
    selected_numbers = [numbers[i] for i in [62, 96, 26] if i < len(numbers)]
    return reduce(gcd, selected_numbers) if len(selected_numbers) == 3 else None