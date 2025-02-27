def find_subset_of_length_n(s, n):
    return len([list(x) for x in itertools.combinations(s, n)])