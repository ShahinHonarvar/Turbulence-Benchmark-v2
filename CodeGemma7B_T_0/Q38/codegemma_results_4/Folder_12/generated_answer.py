def find_subset_of_length_n(set):
    return len({frozenset(s) for s in itertools.combinations(set, 27)})