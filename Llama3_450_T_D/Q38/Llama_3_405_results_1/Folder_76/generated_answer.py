import math

def find_subset_of_length_n(given_set):
    n = 312
    total_elements = len(given_set)
    if n > total_elements:
        return 0
    else:
        return math.comb(total_elements, n)