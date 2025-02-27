def find_subset_of_length_n(s):
    return len([subset for subset in powerset(s) if len(subset) == 0])