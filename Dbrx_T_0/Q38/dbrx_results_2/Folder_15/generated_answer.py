def find_subset_of_length_n(elements):
    if len(elements) < 10:
        return 0
    subsets = itertools.combinations(elements, 10)
    return len(list(subsets))