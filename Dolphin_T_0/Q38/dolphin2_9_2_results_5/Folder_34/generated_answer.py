def find_subset_of_length_n(s):
    return len([c for i, a in enumerate(s, 2) for c in combinations(s, i) if len(c) == 97])