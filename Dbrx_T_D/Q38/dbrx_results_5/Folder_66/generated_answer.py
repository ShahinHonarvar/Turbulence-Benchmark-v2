def find_subset_of_length_n(input_set):
    if len(input_set) < 42:
        return 0
    else:
        return len(list(itertools.combinations(input_set, 42)))