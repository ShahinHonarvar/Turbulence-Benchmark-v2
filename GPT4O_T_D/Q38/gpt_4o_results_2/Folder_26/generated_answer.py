import math

def find_subset_of_length_n(elements_set):
    n = len(elements_set)
    if n < 25:
        return 0
    return math.comb(n, 25)