from math import comb

def find_subset_of_length_n(set_of_elements):
    if len(set_of_elements) < 80:
        return 0
    return comb(len(set_of_elements), 80)