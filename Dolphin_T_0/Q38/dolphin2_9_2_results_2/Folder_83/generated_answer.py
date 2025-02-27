def find_subset_of_length_n(s):
    if len(s) < 95:
        return 0
    return s.combination(95).count()