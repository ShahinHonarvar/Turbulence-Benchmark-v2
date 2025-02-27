import math

def find_subset_of_length_n(s):
    n = len(s)
    r = 312
    if n < r:
        return 0
    else:
        return math.comb(n, r)