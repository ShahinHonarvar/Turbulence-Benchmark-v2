import math

def find_subset_of_length_n(input_set):
    set_length = len(input_set)
    combination = math.comb(set_length, 97)
    return combination