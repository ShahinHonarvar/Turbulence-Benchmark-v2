def find_subset_of_length_n(elements):
    if len(elements) < 47:
        return 0
    subsets = itertools.combinations(elements, 47)
    return len(list(subsets))