from math import comb

def find_subset_of_length_n(s):
    return comb(len(s), 83) if len(s) >= 83 else 0