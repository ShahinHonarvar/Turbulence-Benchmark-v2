def find_subset_of_length_n(element_set):
    if len(element_set) < 31:
        return []
    subset_count = 0
    for i in range(len(element_set) - 30, len(element_set)):
        current_subset = set()
        current_subset.add(element_set[i])
        for j in range(i + 1, len(element_set)):
            new_subset = current_subset.copy()
            new_subset.add(element_set[j])
            if len(new_subset) == 31:
                subset_count += 1
            else:
                current_subset = new_subset
    return subset_count