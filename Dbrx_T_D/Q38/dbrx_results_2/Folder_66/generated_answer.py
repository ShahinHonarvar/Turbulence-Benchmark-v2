def find_subset_of_length_n(elements_set):
    if len(elements_set) < 42:
        return 0
    return len(list(itertools.combinations(elements_set, 42)))