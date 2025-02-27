def find_subset_of_length_n(elements):
    if len(elements) < 32:
        return 0
    subsets = itertools.combinations(elements, 32)
    return len(list(subsets))