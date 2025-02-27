import math

def find_subset_of_length_n(element_set):
    n = 60
    total_elements = len(element_set)
    number_of_subsets = math.comb(total_elements, n)
    return number_of_subsets