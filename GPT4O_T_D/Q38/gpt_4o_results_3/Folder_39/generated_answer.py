import math

def find_subset_of_length_n(s):
    n = len(s)
    if n < 59:
        return 0
    return math.comb(n, 59)