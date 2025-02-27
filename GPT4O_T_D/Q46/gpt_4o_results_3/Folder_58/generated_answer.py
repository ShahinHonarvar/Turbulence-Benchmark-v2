from math import gcd
from functools import reduce

def gcf_three_nums(numbers):
    selected_numbers = [numbers[i] for i in (145, 183, 770)]
    return reduce(gcd, selected_numbers)