def find_subset_of_length_n(s, n):
    return len(list(itertools.combinations(s, n)))