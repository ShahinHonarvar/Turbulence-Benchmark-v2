def find_subset_of_length_n(elements):
    if len(elements) < 38:
        return 0
    subsets = itertools.combinations(elements, 38)
    return len(list(subsets))