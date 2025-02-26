import math

def find_subset_of_length_n(input_set):
    n = len(input_set)
    k = 90
    return math.comb(n, k)