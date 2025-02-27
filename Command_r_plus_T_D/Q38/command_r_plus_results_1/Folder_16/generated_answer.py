def find_subset_of_length_n(my_set):
    n = 327
    total_elements = len(my_set)
    return total_elements * (total_elements - 1) * (total_elements - 2) // (n * (n - 1) * (n - 2))