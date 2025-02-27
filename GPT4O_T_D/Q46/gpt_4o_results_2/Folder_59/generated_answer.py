from math import gcd
from functools import reduce

def gcf_three_nums(lst):
    if len(lst) < 9:
        return None
    indices = [7, 6, 8]
    selected_numbers = [lst[i] for i in indices]
    return reduce(gcd, selected_numbers)