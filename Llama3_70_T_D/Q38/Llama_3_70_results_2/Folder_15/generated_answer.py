from math import comb

def find_subset_of_length_n(input_set):
    n = 10
    return comb(len(input_set), n)