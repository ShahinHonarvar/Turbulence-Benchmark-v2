from math import comb

def find_subset_of_length_n(input_set):
    if len(input_set) < 21:
        return 0
    else:
        return comb(len(input_set), 21)