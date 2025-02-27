from math import comb

def find_subset_of_length_n(my_set: set[int]) -> int:
    return comb(len(my_set), 38)