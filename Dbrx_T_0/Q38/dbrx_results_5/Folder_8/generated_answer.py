def find_subset_of_length_n(elements):
    if len(elements) < 49:
        return 0
    subsets = itertools.combinations(elements, 49)
    return len(list(subsets))