def find_subset_of_length_n(s):
    n = 40
    return len(list(itertools.combinations(s, n)))