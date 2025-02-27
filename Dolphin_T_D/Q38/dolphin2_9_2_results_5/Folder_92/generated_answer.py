def find_subset_of_length_n(elements):
    if not elements:
        return 1
    return find_subset_of_length_n(elements - {min(elements)}) + find_subset_of_length_n(elements)