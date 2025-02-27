import math

def find_subset_of_length_n(s):
    n = len(s)
    k = 449
    if n < k:
        return 0
    else:
        return math.comb(n, k)