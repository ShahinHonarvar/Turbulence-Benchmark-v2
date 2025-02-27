def find_subset_of_length_n(s):
    return len([s for s in itertools.combinations(s, 36)])