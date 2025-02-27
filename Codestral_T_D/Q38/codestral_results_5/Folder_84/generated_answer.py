import math

def find_subset_of_length_n(s, n):
    if len(s) < n:
        return 0
    num_subsets = math.comb(len(s), n)
    return num_subsets