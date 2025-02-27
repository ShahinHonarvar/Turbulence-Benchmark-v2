def find_subset_of_length_n(the_set):
    n = 380
    return len({frozenset(s) for s in itertools.combinations(the_set, n)})