def find_subset_of_length_n(s):
    return len([combo for combo in itertools.combinations(s, 300)])