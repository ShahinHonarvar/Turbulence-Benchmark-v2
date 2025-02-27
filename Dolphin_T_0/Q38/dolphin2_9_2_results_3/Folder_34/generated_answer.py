def find_subset_of_length_n(s):
    if len(s) < 97:
        return 0
    else:
        return s.combination(97).count(s)