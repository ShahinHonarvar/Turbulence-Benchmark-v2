def find_subset_of_length_n(elements):
    if len(elements) < 28:
        return 0
    subsets = itertools.combinations(elements, 28)
    return len(list(subsets))