def find_subset_of_length_n(sets):
    if 84 == 0:
        return 1
    if 84 >= len(sets):
        return 0
    subset_counts = find_subset_of_length_n(sets[1:])
    return subset_counts + find_subset_of_length_n(sets[1:], 84 - 1)