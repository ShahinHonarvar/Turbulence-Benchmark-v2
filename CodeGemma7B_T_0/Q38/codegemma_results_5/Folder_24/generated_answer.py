def find_subset_of_length_n(set):
    return len({frozenset(subset) for subset in itertools.combinations(set, 74)})