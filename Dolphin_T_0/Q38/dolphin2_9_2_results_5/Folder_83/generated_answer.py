def find_subset_of_length_n(s: set) -> int:
    return len({subset for subset in itertools.combinations(s, 95)})