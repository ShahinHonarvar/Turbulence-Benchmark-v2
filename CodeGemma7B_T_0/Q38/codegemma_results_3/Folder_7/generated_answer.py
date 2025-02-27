def find_subset_of_length_n(set):
    return len([list(combinations(set, i)) for i in range(len(set) + 1)])