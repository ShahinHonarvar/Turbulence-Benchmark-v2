import math

def find_subset_of_length_n(s):
    n = len(s)
    return nCr(n, 63)

def nCr(n, r):
    return math.comb(n, r)