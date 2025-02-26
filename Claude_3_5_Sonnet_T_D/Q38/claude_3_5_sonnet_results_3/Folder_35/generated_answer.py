from math import comb

def find_subset_of_length_n(input_set):
    set_size = len(input_set)
    subset_size = 300
    return comb(set_size, subset_size)