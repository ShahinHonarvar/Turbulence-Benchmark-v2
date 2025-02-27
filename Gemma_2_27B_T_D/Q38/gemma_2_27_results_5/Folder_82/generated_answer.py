def find_subset_of_length_n(s):
    n = 83
    return len([subset for subset in iter(lambda: next(itertools.combinations(s, n)), ())])