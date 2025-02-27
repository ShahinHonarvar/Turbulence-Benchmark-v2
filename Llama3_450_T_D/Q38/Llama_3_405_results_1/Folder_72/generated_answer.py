import math

def find_subset_of_length_n(elements):
    n = 16
    return math.comb(len(elements), n)