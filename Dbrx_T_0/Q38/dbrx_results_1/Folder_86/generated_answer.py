def find_subset_of_length_n(elements):
    if len(elements) < 380:
        return 0
    subsets = itertools.combinations(elements, 380)
    return len(list(subsets))