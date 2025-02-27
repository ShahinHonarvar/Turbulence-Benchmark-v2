import math

def find_subset_of_length_n(s):
    if len(s) < 94:
        return 0
    else:
        return math.comb(len(s), 94)