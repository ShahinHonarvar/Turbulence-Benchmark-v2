def find_subset_of_length_n(set_a):
    return len({tuple(s) for s in itertools.combinations(set_a, 327)})