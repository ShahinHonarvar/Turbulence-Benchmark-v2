import math

def find_subset_of_length_n(set_elements: set) -> int:
    n = len(set_elements)
    return math.comb(n, 860)