def find_subset_of_length_n(my_set):
    length = len(my_set)
    return length * (length - 1) * (length - 2) // 6