import math

def find_subset_of_length_n(s):
    n = len(s)
    r = 360
    return math.comb(n, r)