def find_subset_of_length_n(s):
    n = 30
    return len(list(itertools.combinations(s, n)))