def find_subset_of_length_n(given_set):
    return len({frozenset(row) for row in itertools.combinations(given_set, 47)})