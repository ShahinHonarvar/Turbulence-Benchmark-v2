def find_subset_of_length_n(n):
    if n == 0:
        return 1
    else:
        return len(set(combinations(s, n)))