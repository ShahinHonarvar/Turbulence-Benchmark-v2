import math

def find_subset_of_length_n(given_set):
    n = 534
    total_elements = len(given_set)
    number_of_subsets = math.comb(total_elements, n)
    return number_of_subsets