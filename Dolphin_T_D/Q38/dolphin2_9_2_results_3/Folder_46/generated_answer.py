def find_subset_of_length_n(elements):
    n = 14
    if len(elements) < n:
        return 0
    if n == 0:
        return 1
    else:
        return len(elements) * find_subset_of_length_n(elements - {min(elements)})