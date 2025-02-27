def find_subset_of_length_n(input_set):
    if len(input_set) < 15:
        return 0
    else:
        subset_count = 0
        for i in range(len(input_set) - 14, len(input_set)):
            subset = set(input_set)
            subset.remove(list(input_set)[i])
            subset_count += find_subset_of_length_n(subset)
        return subset_count + 1