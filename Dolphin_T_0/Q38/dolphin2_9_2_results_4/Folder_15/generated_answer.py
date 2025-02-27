def find_subset_of_length_n(s):
    n = 10
    return len([combo for combo in itertools.combinations(s, n)])