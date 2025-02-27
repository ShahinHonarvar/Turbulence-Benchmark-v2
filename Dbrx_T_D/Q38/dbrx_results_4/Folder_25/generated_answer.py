def find_subset_of_length_n(elements):
    if len(elements) < 90:
        return 0
    subsets = itertools.combinations(elements, 90)
    return len(list(subsets))