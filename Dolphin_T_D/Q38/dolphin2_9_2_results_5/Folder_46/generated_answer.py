def find_subset_of_length_n(s):
    return len([subset for subset in chain.from_iterable((combinations(s, r) for r in range(15))) if len(subset) == 14])