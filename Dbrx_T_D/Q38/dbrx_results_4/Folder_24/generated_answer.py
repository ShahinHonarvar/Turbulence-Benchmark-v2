def find_subset_of_length_n(s, n=74):
    return sum((1 for subset in itertools.combinations(s, n)))