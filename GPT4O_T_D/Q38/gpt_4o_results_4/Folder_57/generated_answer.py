import math

def find_subset_of_length_n(s):
    n = 92
    set_length = len(s)
    if set_length < n:
        return 0
    return math.comb(set_length, n)