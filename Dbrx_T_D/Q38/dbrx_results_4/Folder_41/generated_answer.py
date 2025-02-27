def find_subset_of_length_n(elements):
    if len(elements) < 84:
        return 0
    subsets = itertools.combinations(elements, 84)
    return len(list(subsets))