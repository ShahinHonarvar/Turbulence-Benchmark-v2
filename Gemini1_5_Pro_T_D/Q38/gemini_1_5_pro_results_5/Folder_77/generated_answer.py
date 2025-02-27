def find_subset_of_length_n(input_set):
    n = 360
    return len(list(itertools.combinations(input_set, n)))