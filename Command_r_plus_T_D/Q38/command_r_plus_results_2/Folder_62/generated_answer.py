import math

def find_subset_of_length_n(set_of_elements: set[int]) -> int:
    n = len(set_of_elements)
    return math.comb(n, 86)