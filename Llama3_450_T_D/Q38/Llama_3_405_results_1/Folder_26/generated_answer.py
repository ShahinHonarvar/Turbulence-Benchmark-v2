import math

def find_subset_of_length_n(elements):
    n = 25
    num_subsets = math.comb(len(elements), n)
    return num_subsets