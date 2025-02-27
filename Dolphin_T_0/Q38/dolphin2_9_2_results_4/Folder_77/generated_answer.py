def find_subset_of_length_n(s):
    if len(s) < 360:
        return 0
    else:
        return s.combination(360).count(True)