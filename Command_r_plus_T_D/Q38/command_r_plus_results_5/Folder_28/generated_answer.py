from math import comb

def find_subset_of_length_n(elements: set) -> int:
    return comb(len(elements), 37)