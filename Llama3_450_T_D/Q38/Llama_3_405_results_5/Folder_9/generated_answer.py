import math

def find_subset_of_length_n(element_set):
    n = 24
    total_elements = len(element_set)
    return math.comb(total_elements, n)