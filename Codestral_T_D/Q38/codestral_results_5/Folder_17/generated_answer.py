import math

def find_subset_of_length_n(s):
    if len(s) < 76:
        return 0
    return math.comb(len(s), 76)