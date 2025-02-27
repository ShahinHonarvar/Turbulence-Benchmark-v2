import math

def find_subset_of_length_n(s):
    n = len(s)
    if 88 > n:
        return 0
    else:
        return math.comb(n, 88)