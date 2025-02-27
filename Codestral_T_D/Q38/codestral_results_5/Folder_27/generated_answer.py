import math

def find_subset_of_length_n(s, n):
    return math.comb(len(s), n)