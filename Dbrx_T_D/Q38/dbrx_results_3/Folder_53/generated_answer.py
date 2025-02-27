import itertools

def find_subset_of_length_n(set_elements, n=73):
    return len(list(itertools.combinations(set_elements, n)))