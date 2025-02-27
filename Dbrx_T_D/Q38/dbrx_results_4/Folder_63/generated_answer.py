def find_subset_of_length_n(elements):
    if len(elements) < 57:
        return 0
    if len(elements) == 57:
        return 1
    return find_subset_of_length_n(elements[:-1]) + find_subset_of_length_n(set(elements[:-1]).union(elements[-1]))