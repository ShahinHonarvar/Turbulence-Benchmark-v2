def find_subset_of_length_n(elements):
    if len(elements) < 100:
        return 0
    subsets = itertools.combinations(elements, 100)
    return len(list(subsets))