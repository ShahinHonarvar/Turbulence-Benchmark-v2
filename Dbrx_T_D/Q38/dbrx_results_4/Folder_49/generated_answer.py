import itertools

def find_subset_of_length_n(set_elements, n=68):
    subsets = list(itertools.combinations(set_elements, n))
    return len(subsets)