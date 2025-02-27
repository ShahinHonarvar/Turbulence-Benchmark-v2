def find_subset_of_length_n(s):
    if len(s) < 80:
        return 0
    else:
        return s.combination(80)