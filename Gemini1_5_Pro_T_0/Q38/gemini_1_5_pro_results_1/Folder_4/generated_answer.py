def find_subset_of_length_n(input_set):
    n = 15
    return len(list(itertools.combinations(input_set, n)))