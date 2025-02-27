from math import comb

def find_subset_of_length_n(element_set):
    n = 2
    return comb(len(element_set), n)