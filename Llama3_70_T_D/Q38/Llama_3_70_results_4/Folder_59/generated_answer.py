def find_subset_of_length_n(s):
    return len([subset for subset in __import__('itertools').combinations(s, 2)])