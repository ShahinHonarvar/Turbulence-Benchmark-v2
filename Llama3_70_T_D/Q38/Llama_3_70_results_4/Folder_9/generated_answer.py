import math

def find_subset_of_length_n(input_set):
    n = len(input_set)
    return math.comb(n, 24)