import math

def find_subset_of_length_n(given_set):
    n = len(given_set)
    k = 21
    return math.comb(n, k)