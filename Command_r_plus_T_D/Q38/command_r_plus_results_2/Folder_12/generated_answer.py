import math

def find_subset_of_length_n(elements: set) -> int:
    n = len(elements)
    return math.comb(n, 27)