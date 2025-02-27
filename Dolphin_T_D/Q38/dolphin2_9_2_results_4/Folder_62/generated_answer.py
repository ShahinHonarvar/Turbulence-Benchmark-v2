def find_subset_of_length_n(s):
    return len([subset for subset in chain(*[combinations(s, r) for r in range(87)]) if len(subset) == 86])