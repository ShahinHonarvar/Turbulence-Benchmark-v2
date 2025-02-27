import math

def find_subset_of_length_n(elements):
    n = 8
    return math.comb(len(elements), n)