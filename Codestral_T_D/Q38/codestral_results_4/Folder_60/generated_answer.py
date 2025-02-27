import math

def find_subset_of_length_n(s):
    n = len(s)
    k = 88
    return math.comb(n, k)