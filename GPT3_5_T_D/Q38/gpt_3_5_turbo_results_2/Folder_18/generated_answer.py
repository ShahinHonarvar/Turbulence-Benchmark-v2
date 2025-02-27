import itertools

def find_subset_of_length_n(elements):
    subsets = set(itertools.combinations(elements, 630))
    return len(subsets)