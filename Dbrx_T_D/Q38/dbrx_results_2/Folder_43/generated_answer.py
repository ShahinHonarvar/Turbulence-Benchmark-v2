from math import comb

def find_subset_of_length_n(elements):
    num_subsets = comb(len(elements), 29)
    return num_subsets