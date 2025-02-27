from math import comb

def find_subset_of_length_n(elements: set) -> int:
    n = len(elements)
    return comb(n, 85)