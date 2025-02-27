def find_subset_of_length_n(s):
    return len(filter(lambda x: len(x) == 327, combinations(s, 327)))