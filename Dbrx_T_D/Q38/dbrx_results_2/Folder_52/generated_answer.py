def find_subset_of_length_n(input_set):
    if len(input_set) < 32:
        return 0
    subsets = itertools.combinations(input_set, 32)
    return len(list(subsets))