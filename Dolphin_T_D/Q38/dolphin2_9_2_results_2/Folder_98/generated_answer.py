def find_subset_of_length_n(a_set):
    length = len(a_set)
    return length * (length - 1) * (length - 2) * (length - 3) // 24