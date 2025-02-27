def find_subset_of_length_n(elements):
    if len(elements) < 8:
        return 0
    subsets = itertools.combinations(elements, 8)
    return len(list(subsets))