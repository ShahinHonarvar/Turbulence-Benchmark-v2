def find_subset_of_length_n(s):
    return len([subset for subset in [set(combination) for combination in itertools.combinations(s, 3)] if len(subset) == 3])