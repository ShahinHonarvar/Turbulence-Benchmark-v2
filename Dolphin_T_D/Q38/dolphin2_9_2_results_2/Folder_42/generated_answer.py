def find_subset_of_length_n(S):
    return len([subset for subset in itertools.combinations(S, 31)])