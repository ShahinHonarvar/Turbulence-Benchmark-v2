import math

def find_subset_of_length_n(s):
    if len(s) >= 73:
        return math.comb(len(s), 73)
    else:
        return 0