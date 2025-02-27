def find_subset_of_length_n(input_set):
    n = 34
    return len([subset for subset in set(itertools.combinations(input_set, n))])