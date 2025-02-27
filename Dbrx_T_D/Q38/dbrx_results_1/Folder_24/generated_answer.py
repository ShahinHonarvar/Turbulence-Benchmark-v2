def find_subset_of_length_n(s):
    if len(s) < 74:
        return 0
    else:
        return len(list(itertools.combinations(s, 74)))