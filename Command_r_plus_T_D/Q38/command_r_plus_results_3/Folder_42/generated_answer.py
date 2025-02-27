import math

def find_subset_of_length_n(elements_set: set) -> int:
    total_elements = len(elements_set)
    return math.comb(total_elements, 31)