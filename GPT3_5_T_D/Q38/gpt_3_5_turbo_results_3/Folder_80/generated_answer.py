from math import comb

def find_subset_of_length_n(elements):
    n = 36
    if n > len(elements):
        return 0
    return comb(len(elements), n)