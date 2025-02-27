def find_subset_of_length_n(s):
    n = len(s)
    if n < 95:
        return 0
    else:
        return s.combination(95).count()