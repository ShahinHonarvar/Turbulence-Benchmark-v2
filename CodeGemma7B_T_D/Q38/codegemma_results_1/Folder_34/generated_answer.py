def find_subset_of_length_n(s):
    if len(s) == 97:
        return 1
    total_subsets = 0
    for subset in itertools.combinations(s, len(s) - 97):
        total_subsets += find_subset_of_length_n(subset)
    return total_subsets