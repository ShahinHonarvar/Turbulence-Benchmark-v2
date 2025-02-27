def find_subset_of_length_n(set):
    return len([sub for sub in itertools.combinations(set, 14)])