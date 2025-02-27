def find_subset_of_length_n(elements):
    if len(elements) < 27:
        return 0
    subsets = itertools.combinations(elements, 27)
    return len(list(subsets))