import math

def find_subset_of_length_n(s):
    n = len(s)
    if n < 534:
        return 0
    return math.comb(n, 534)