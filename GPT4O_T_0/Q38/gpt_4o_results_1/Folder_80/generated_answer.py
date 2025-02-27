import math

def find_subset_of_length_n(elements):
    if len(elements) < 36:
        return 0
    return math.comb(len(elements), 36)