import math

def find_subset_of_length_n(elements_set):
    if len(elements_set) < 360:
        return 0
    return math.comb(len(elements_set), 360)