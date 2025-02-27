def find_subset_of_length_n(s):
    n = 6
    return len([set(x) for x in itertools.combinations(s, n)])