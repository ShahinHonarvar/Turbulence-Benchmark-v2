def find_subset_of_length_n(s):
    size = 47
    return len([c for c in itertools.combinations(s, size)])