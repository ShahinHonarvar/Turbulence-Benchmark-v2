def find_subset_of_length_n(elements_set, n):
    if n < 0 or n > len(elements_set):
        return 0
    if n == 0 or n == len(elements_set):
        return 1
    elements_set_modified = tuple(elements_set)
    subsets_count = 0
    for i in range(len(elements_set_modified) - n + 1):
        current_subset = elements_set_modified[i:i + n]
        if len(current_subset) == n:
            subsets_count += 1
    return subsets_count