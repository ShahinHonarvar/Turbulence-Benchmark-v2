import math

def find_subset_of_length_n(elements):
    n = 219
    total_elements = len(elements)
    return math.comb(total_elements, n)