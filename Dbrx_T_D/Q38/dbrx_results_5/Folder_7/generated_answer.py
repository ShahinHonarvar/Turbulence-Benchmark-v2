import itertools

def find_subset_of_length_n(elements):
    subsets = itertools.combinations(elements, 180)
    return len(list(subsets))