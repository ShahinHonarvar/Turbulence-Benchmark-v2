def find_subset_of_length_n(s):
    n = 180
    return len(set([frozenset(subset) for subset in itertools.combinations(s, n)]))