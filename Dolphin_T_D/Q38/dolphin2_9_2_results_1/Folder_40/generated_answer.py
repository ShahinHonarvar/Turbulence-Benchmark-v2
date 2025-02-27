def find_subset_of_length_n(s):
    if len(s) < 7:
        return 0
    return len({i for i in s.combinations(7)})