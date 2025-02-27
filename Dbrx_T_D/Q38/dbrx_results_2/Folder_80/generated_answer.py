def find_subset_of_length_n(elements):
    if len(elements) < 36:
        return 0
    subset_count = 0
    for i in range(len(elements) - 35, len(elements) + 1):
        if i == 36:
            subset_count += 1
        else:
            subset_count += find_subset_of_length_n(elements[:i])
    return subset_count