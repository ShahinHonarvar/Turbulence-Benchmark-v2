import itertools

def find_subset_of_length_n(s):
    subsets = list(itertools.combinations(s, 97))
    return len(subsets)