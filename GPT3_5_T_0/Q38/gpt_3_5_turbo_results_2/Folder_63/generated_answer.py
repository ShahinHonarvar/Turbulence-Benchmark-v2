import itertools

def find_subset_of_length_n(elements):
    subsets = list(itertools.combinations(elements, 57))
    return len(subsets)