def find_subset_of_length_n(s: set) -> int:
    return len([c for i in range(631) for c in s.combinations(i)])