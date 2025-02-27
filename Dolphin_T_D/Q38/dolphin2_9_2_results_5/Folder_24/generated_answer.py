def find_subset_of_length_n(elements):
    n = 74
    if n > len(elements):
        return 0
    else:
        return len(elements) * find_subset_of_length_n(elements[1:])