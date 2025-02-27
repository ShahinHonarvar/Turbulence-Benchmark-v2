def find_subset_of_length_n(s):
    if len(s) < 77:
        return 0
    return s.combination(77).count(s)