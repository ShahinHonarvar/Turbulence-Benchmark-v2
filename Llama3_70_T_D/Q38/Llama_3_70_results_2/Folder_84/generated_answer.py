import math

def find_subset_of_length_n(element_set):
    set_length = len(element_set)
    combination_size = 872
    result = math.comb(set_length, combination_size)
    return result