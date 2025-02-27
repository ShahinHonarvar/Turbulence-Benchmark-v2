import math

def find_subset_of_length_n(input_set):
    return math.comb(len(input_set), 33) if len(input_set) >= 33 else 0