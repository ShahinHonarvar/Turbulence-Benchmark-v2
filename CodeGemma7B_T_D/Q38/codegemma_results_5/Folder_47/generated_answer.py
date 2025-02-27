def find_subset_of_length_n(set1):
    if len(set1) != 34:
        raise ValueError('Set size cannot be 34')
    num_subsets = 2 ** len(set1)
    return num_subsets