def find_subset_of_length_n(s):
    return len([1 for i in range(len(s) + 1) for _ in combinations(s, i) if i == 7])