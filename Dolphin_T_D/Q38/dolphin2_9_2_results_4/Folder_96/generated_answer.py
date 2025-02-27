def find_subset_of_length_n(s):
    if not isinstance(s, set):
        raise ValueError('Input should be a set')
    return len([c for c in combinations(s, 47)])