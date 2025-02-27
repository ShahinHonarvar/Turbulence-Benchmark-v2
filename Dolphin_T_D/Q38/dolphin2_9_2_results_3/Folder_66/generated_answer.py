def find_subset_of_length_n(S):
    return len([subset for subset in chain.from_iterable((combinations(S, r) for r in range(len(S) + 1))) if len(subset) == 42])