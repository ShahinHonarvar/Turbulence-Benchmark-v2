def find_subset_of_length_n(s):
    n = 752
    return len([subset for subset in [set(combination) for combination in itertools.combinations(s, n)] if len(subset) == n and subset.issubset(s)])