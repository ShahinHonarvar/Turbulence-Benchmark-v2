def find_subset_of_length_n(s, n=59):
    return len([c for c in s if len(c) == n])