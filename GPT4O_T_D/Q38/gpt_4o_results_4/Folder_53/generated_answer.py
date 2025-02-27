import math

def find_subset_of_length_n(s):
    return math.comb(len(s), 73) if len(s) >= 73 else 0