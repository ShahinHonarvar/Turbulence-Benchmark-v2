def find_subset_of_length_n(s):
    """Computes the number of all subsets of size 74 in a set s."""
    return len([subset for subset in itertools.combinations(s, 74)])