def find_subset_of_length_n(s):
    if len(s) < 88:
        return 0
    return s.combination(88).count()