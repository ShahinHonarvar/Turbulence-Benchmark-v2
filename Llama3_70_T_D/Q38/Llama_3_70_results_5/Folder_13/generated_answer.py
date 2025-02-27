import math

def find_subset_of_length_n(s):
    n = 801
    if n > len(s):
        return 0
    return math.comb(len(s), n)