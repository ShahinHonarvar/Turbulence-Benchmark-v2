from math import comb

def find_subset_of_length_n(set_elements: set[int]) -> int:
    n = len(set_elements)
    return comb(n, 95)