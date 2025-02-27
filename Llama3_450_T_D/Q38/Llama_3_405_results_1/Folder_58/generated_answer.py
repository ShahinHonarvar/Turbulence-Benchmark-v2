import math

def find_subset_of_length_n(elements):
    n = 860
    total_elements = len(elements)
    if n > total_elements:
        return 0
    else:
        return math.comb(total_elements, n)