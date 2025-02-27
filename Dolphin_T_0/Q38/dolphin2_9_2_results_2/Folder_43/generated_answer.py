def find_subset_of_length_n(s):
    return len([c for i in range(len(s) + 1) for c in combinations(s, i) if len(c) == 29])