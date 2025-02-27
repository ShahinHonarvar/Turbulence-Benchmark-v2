def find_subset_of_length_n(subset_size, elements):
    if subset_size == 0:
        return 1
    if subset_size > len(elements):
        return 0
    return find_subset_of_length_n(subset_size - 1, elements[1:]) + find_subset_of_length_n(subset_size, elements[1:])