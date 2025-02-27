import math

def find_subset_of_length_n(elements):
    n = 752
    if len(elements) < n:
        return 0
    return math.comb(len(elements), n)