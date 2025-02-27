def find_subset_of_length_n(set):
    length = 0
    for subset in powerset(set):
        length += len(subset) == 327
    return length