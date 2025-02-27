import math

def find_subset_of_length_n(element_set):
    n = len(element_set)
    subset_size = 801
    return math.comb(n, subset_size)