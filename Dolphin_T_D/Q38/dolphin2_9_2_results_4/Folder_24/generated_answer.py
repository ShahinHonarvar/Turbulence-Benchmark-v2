def find_subset_of_length_n(s):
    if len(s) < 74:
        return 0
    subset_size = len(s)
    for i in range(74, subset_size + 1):
        subset_length = len(s)
        for j in range(subset_length - i + 1, subset_length + 1):
            s.subset = list(combinations(s, j))
    return len(s.subset)