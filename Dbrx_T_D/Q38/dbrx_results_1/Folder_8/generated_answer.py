def find_subset_of_length_n(input_set):
    return sum((1 for subset in itertools.combinations(input_set, 49)))