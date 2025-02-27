def find_subset_of_length_n(elements):
    length = 36
    if length > len(elements):
        return 0
    return len(list(combinations(elements, length)))