from math import comb

def find_subset_of_length_n(elements):
    if len(elements) < 18:
        return 0
    return comb(len(elements), 18)