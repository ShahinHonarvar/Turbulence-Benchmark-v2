import math

def find_subset_of_length_n(elements: set[int]) -> int:
    n = len(elements)
    return math.comb(n, 793)