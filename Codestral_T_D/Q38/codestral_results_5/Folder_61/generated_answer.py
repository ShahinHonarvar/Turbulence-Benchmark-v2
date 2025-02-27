import math

def find_subset_of_length_n(elements):
    n = len(elements)
    k = 8
    return math.comb(n, k)