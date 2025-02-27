import math

def find_subset_of_length_n(element_set):
    n = 74
    total_elements = len(element_set)
    if n > total_elements:
        return 0
    else:
        return math.comb(total_elements, n)