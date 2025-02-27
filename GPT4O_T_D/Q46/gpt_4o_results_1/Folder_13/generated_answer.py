from math import gcd
from functools import reduce

def gcf_three_nums(lst):
    selected_elements = [lst[i] for i in (991, 244, 974)]
    return reduce(gcd, selected_elements)