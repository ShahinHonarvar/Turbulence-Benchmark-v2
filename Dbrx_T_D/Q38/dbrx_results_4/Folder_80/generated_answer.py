def find_subset_of_length_n(elements_set):
    if not isinstance(elements_set, set) or len(elements_set) < 36:
        return 0
    return len(list(itertools.combinations(elements_set, 36)))