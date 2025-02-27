def find_subset_of_length_n(elements):
    if len(elements) < 18:
        return 0
    subsets = itertools.combinations(elements, 18)
    return len(list(subsets))