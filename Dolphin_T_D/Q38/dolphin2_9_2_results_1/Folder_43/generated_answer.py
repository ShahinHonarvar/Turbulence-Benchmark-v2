def find_subset_of_length_n(s: set) -> int:
    n = 29
    return len([c for c in combinations(s, n)])