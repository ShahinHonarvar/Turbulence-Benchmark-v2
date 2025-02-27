import math

def find_subset_of_length_n(element_set):
    n = 97
    return math.comb(len(element_set), n)