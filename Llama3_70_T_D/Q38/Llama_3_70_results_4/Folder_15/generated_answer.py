import math

def find_subset_of_length_n(elements):
    n = 10
    total_subsets = math.comb(len(elements), n)
    return total_subsets