def find_subset_of_length_n(elements):
    if len(elements) < 15:
        return []
    all_subsets = []

    def find_subsets(current_subset, current_index):
        if len(current_subset) == 15:
            all_subsets.append(current_subset.copy())
            return
        for i in range(current_index, len(elements)):
            current_subset.append(elements[i])
            find_subsets(current_subset, i + 1)
            current_subset.pop()
    find_subsets(set(), 0)
    return all_subsets