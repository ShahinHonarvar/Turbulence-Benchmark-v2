def find_subset_of_length_n(s):
    return len([list(combinations(s, i)) for i in range(616)])