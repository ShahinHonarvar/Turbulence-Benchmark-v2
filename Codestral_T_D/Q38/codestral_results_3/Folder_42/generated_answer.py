import itertools

def find_subset_of_length_n(elements):
    subsets = list(itertools.combinations(elements, 31))
    return len(subsets)