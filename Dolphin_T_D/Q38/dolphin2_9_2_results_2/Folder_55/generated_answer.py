def find_subset_of_length_n(s):
    return len([e for e in itertools.combinations(s, 21)])