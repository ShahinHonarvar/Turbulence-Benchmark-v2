def find_subset_of_length_n(elements):
    if len(elements) < 180:
        return 0
    subsets = itertools.combinations(elements, 180)
    return len(list(subsets))