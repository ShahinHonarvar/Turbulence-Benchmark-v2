import math

def find_subset_of_length_n(given_set):
    n = len(given_set)
    r = 372
    return math.comb(n, r)