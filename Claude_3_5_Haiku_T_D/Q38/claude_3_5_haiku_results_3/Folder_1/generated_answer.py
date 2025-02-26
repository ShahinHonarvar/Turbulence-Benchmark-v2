from math import comb

def find_subset_of_length_n(input_set):
    total_elements = len(input_set)
    return comb(total_elements, 85)