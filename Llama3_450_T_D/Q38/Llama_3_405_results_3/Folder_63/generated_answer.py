import math

def find_subset_of_length_n(given_set):
    n = len(given_set)
    r = 57
    return math.comb(n, r)