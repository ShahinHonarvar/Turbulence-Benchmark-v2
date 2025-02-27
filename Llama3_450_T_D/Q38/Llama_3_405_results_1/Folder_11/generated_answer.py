import math

def find_subset_of_length_n(element_set):
    n = len(element_set)
    k = 77
    return math.comb(n, k)