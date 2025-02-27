def find_subset_of_length_n(s, n=380):
    return len(list(itertools.combinations(s, n)))