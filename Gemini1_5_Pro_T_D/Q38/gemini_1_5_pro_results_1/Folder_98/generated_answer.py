def find_subset_of_length_n(set1):
    return len(set([subset for subset in powerset(set1) if len(subset) == 4]))