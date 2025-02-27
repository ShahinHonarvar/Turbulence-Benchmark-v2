def find_subset_of_length_n(s):
    return len([subset for subset in itertools.product(s, repeat=7)])