from math import comb

def find_subset_of_length_n(elements):
    total_elements = len(elements)
    return comb(total_elements, 60)