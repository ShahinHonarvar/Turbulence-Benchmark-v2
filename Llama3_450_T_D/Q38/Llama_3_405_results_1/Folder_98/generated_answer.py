import itertools

def find_subset_of_length_n(element_set):
    return len(list(itertools.combinations(element_set, 4)))