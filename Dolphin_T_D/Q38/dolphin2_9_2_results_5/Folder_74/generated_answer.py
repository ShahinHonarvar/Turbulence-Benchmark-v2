def find_subset_of_length_n(s: set) -> int:
    n = 48
    return len([c for c in combinations(s, n)])