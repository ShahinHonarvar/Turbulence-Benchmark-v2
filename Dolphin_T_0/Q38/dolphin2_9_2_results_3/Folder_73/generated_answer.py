def find_subset_of_length_n(s):
    return len([subset for subset in chain.from_islice(combinations(s, 41), 0, None, 1)])