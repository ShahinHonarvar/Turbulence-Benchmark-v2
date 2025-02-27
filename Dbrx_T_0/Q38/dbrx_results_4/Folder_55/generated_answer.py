def find_subset_of_length_n(elements):
    if len(elements) < 21:
        return 0
    subsets = itertools.combinations(elements, 21)
    return len(list(subsets))