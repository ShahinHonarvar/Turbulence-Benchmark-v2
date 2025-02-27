def find_subset_of_length_n(set):
    return len({tuple(s) for s in itertools.combinations(set, 28)})