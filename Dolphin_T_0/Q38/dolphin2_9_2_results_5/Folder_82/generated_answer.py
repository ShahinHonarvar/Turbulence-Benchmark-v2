def find_subset_of_length_n(s):
    return len([sub for sub in itertools.combinations(s, 83)])