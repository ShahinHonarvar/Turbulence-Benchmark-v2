import math

def find_subset_of_length_n(elements_set):
    n = len(elements_set)
    return math.comb(n, 78) if n >= 78 else 0