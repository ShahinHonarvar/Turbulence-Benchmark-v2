import math

def find_subset_of_length_n(s):
    n = 64
    return math.comb(len(s), n)