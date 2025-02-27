def find_subset_of_length_n(s):
    n = 793
    return len([subset for subset in set(combinations(s, n))])