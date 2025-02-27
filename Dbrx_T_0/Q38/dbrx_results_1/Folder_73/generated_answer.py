def find_subset_of_length_n(elements):
    if len(elements) < 41:
        return 0
    subsets = itertools.combinations(elements, 41)
    return len(list(subsets))