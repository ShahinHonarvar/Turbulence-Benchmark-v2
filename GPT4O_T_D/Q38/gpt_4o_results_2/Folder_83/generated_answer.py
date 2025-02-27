import math

def find_subset_of_length_n(elements):
    n = len(elements)
    k = 95
    if n < k:
        return 0
    return math.comb(n, k)