import math

def find_subset_of_length_n(elements):
    set_size = len(elements)
    subset_size = 100
    if set_size < subset_size:
        return 0
    return math.comb(set_size, subset_size)