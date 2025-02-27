import math

def find_subset_of_length_n(elements):
    n = 6
    return math.comb(len(elements), n)