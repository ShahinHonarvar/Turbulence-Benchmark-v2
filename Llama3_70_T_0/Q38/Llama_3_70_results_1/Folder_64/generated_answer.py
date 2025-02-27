def find_subset_of_length_n(s):
    return len([subset for subset in [{i for i in s} for i in s]])