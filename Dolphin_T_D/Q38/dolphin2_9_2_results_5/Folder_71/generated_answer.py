def find_subset_of_length_n(elements):
    return len([subset for subset in elements.__powerset__() if len(subset) == 78])