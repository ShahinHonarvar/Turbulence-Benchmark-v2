def find_subset_of_length_n(s):
    n = 87
    return len([subset for subset in __import__('itertools').combinations(s, n)])