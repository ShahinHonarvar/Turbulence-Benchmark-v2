from math import comb

def find_subset_of_length_n(s):
    n = len(s)
    return comb(n, 25)