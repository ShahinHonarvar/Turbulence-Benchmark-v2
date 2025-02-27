def find_subset_of_length_n(elements):
    length = 19
    if length > len(elements):
        return 0
    if length == len(elements):
        return 1
    return len(elements) * find_subset_of_length_n(elements[1:]) + find_subset_of_length_n(elements[:-1])