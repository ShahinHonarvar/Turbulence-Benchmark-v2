from math import comb

def find_subset_of_length_n(my_set: set) -> int:
    n = len(my_set)
    return comb(n, 93)