import math

def find_subset_of_length_n(input_set):
    n = 4
    return math.comb(len(input_set), n)