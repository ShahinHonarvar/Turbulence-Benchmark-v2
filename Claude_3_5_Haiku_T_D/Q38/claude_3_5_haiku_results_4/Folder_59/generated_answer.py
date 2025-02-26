def find_subset_of_length_n(elements):
    return len(set(len(elements) * (len(elements) - 1) // 2))