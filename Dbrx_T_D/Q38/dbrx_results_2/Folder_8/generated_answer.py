from itertools import combinations

def find_subset_of_length_n(elements_set):
    if not isinstance(elements_set, set):
        raise ValueError('The input should be a set')
    return len(list(combinations(elements_set, 49)))