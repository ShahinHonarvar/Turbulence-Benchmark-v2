def find_subset_of_length_n(elements):
    if len(elements) < 83:
        return 0
    subsets = itertools.combinations(elements, 83)
    return len(list(subsets))