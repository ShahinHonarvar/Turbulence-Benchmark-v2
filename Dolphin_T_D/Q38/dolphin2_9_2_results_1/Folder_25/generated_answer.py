def find_subset_of_length_n(s):
    if len(s) < 90:
        return 0
    else:
        return set(combinations(s, 90))