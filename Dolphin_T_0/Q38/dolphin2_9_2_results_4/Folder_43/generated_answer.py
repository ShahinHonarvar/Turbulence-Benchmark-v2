def find_subset_of_length_n(set_elements):
    if len(set_elements) < 29:
        return 0
    subsets_count = 0
    subset = [None] * 29
    index = 0

    def find_subset_of_length_n_helper(subset_index):
        nonlocal subsets_count
        if subset_index == 29:
            subsets_count += 1
            return
        if subset_index < index:
            for i in range(index, len(set_elements)):
                subset[subset_index] = set_elements[i]
                index = i + 1
                find_subset_of_length_n_helper(subset_index + 1)
                index -= 1
    find_subset_of_length_n_helper(0)
    return subsets_count