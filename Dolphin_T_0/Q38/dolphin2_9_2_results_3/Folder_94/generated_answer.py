def find_subset_of_length_n(s):
    if len(s) < 93:
        return 0
    return s.combination(93).count(True)