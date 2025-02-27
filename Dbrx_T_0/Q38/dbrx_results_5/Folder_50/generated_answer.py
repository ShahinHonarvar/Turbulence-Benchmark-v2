def find_subset_of_length_n(elements):
    if len(elements) < 40:
        return 0
    subsets = itertools.combinations(elements, 40)
    return len(list(subsets))