import math

def find_subset_of_length_n(elements):
    n = len(elements)
    if n < 894:
        return 0
    return math.comb(n, 894)