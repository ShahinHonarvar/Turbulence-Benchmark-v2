import math

def find_subset_of_length_n(element_set):
    n = len(element_set)
    if n < 860:
        return 0
    return math.comb(n, 860)