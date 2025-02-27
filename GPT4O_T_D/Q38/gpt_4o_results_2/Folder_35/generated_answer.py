import math

def find_subset_of_length_n(input_set):
    set_size = len(input_set)
    if set_size < 300:
        return 0
    return math.comb(set_size, 300)