def find_subset_of_length_n(set):
    return len([list(s) for s in itertools.combinations(set, n)])