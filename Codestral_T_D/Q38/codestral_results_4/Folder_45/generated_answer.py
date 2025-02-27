import math

def find_subset_of_length_n(input_set):
    n = len(input_set)
    if n < 33:
        return 0
    return math.comb(n, 33)