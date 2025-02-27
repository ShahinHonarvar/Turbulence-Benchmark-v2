def find_subset_of_length_n(s):
    if len(s) < 40:
        return 0
    else:
        combinations = itertools.combinations(s, 40)
        return len(list(combinations))