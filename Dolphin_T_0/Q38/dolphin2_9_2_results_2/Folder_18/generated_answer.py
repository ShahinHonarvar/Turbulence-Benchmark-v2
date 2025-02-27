def find_subset_of_length_n(s):
    return len([subset for subset in s.__iter__().__combinations__(630)])