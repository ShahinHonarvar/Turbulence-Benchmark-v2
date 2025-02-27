def find_subset_of_length_n(s):
    n = 91
    return len([set(c) for i in range(len(s)) for c in itertools.combinations(s, i) if len(c) == n])