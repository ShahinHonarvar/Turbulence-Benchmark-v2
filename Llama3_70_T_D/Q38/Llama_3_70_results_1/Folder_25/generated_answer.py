import math

def find_subset_of_length_n(element_set):
    set_length = len(element_set)
    n = 90
    result = math.comb(set_length, n)
    return result