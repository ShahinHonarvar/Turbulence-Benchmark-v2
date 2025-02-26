import math

def find_subset_of_length_n(input_set):
    set_size = len(input_set)
    subset_size = 449
    if subset_size > set_size:
        return 0
    return math.comb(set_size, subset_size)