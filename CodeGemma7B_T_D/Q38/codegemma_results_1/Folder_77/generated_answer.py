from itertools import combinations

def find_subset_of_length_n(set_of_elements):
    if len(set_of_elements) != 360:
        raise ValueError('The set must have exactly 360 elements.')
    if len(set_of_elements) == 0:
        return 0
    return len(list(combinations(set_of_elements, 360)))