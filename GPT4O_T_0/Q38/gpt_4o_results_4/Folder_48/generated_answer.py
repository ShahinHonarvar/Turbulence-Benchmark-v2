import math

def find_subset_of_length_n(elements):
    if len(elements) < 793:
        return 0
    return math.comb(len(elements), 793)