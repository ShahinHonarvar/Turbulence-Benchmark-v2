def find_subset_of_length_n(elements):
    raw_subsets = itertools.combinations(elements, 96)
    return len(list(raw_subsets))