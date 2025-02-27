def find_subset_of_length_n(s):
    n = 57
    return len([x for i in range(1, min(len(s), n) + 1) for x in combinations(s, i)])