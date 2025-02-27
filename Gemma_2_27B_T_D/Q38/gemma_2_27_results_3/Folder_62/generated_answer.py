def find_subset_of_length_n(s):
    n = 86
    return len([set(x) for x in itertools.combinations(s, n)])