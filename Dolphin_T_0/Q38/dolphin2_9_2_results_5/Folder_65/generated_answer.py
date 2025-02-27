def find_subset_of_length_n(s):
    return len([list(combination) for combination in combinations(s, 35)])