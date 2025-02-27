import math

def find_subset_of_length_n(elements_set: set) -> int:
    n = len(elements_set)
    return math.comb(n, 93)