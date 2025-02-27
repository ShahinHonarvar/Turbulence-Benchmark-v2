def find_subset_of_length_n(lst):
    return len([subset for subset in itertools.combinations(lst, 860)])