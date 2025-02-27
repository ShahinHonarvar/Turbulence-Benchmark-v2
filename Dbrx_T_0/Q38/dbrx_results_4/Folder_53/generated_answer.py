def find_subset_of_length_n(elements):
    if len(elements) < 73:
        return 0
    subsets = itertools.combinations(elements, 73)
    return len(list(subsets))