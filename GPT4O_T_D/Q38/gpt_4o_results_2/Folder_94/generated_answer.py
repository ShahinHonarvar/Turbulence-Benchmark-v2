import math

def find_subset_of_length_n(elements_set):
    set_size = len(elements_set)
    if set_size < 93:
        return 0
    return math.comb(set_size, 93)