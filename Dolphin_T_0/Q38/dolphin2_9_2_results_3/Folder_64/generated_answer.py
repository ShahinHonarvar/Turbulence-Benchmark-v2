def find_subset_of_length_n(s):
    return len([subset for subset in s if len(subset) == 1])