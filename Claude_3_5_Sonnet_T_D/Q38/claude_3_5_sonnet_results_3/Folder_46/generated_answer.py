from math import comb

def find_subset_of_length_n(elements):
    set_size = len(elements)
    subset_size = 14
    return comb(set_size, subset_size)