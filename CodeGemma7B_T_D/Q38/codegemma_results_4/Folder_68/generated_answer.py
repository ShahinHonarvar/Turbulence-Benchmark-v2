def find_subset_of_length_n(x):
    return sum((1 for subset in itertools.combinations(x, 3)))