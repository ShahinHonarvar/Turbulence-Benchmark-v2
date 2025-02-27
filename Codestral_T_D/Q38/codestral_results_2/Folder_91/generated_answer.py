import math

def find_subset_of_length_n(s, n=6):
    if len(s) < n:
        return 0
    else:
        return math.comb(len(s), n)