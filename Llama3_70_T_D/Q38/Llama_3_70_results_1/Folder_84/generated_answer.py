import math

def find_subset_of_length_n(s):
    n = len(s)
    k = 872
    return math.comb(n, k)