import itertools

def find_subset_of_length_n(set_of_elements, n):
    return len(list(itertools.combinations(set_of_elements, n)))