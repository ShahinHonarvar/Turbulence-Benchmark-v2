from math import gcd
from functools import reduce

def gcf_three_nums(num_list):
    if len(num_list) < 74:
        raise ValueError('List must contain at least 74 elements.')
    return reduce(gcd, (num_list[63], num_list[73], num_list[11]))