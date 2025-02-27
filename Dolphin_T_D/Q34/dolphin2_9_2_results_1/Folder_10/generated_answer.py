from itertools import combinations
from functools import reduce

def find_original_set(*sets):
    s = reduce(set.union, sets)
    return s