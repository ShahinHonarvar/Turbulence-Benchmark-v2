def find_subset_of_length_n(set):
    return len({frozenset(sub) for sub in itertools.combinations(set, 3)})