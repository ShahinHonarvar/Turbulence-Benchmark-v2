from math import comb

def find_subset_of_length_n(set_of_elements):
    set_size = len(set_of_elements)
    return comb(set_size, 300)