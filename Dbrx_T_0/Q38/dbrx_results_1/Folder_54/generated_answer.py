def find_subset_of_length_n(elements):
    if len(elements) < 51:
        return 0
    subsets = itertools.combinations(elements, 51)
    return len(list(subsets))