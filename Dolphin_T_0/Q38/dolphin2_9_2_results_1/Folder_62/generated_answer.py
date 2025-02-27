def find_subset_of_length_n(s):
    if not isinstance(s, set):
        return 'Input must be a set'
    n = 86
    return len([c for c in itertools.combinations(s, n)])