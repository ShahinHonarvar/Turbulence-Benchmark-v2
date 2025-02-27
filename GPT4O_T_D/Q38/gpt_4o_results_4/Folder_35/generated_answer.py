import math

def find_subset_of_length_n(elements):
    if len(elements) < 300:
        return 0
    n = len(elements)
    k = 300
    return math.comb(n, k)