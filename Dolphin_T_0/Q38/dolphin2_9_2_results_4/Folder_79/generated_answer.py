def find_subset_of_length_n(s):
    return len([c for c in chain.from_iterable((combinations(s, r) for r in range(len(s) + 1))) if len(c) == 63])