def find_subset_of_length_n(elements):
    if len(elements) < 793:
        return 0
    subsets_count = 0
    for i in range(len(elements) - 792):
        for j in range(i + 1, len(elements) - 791):
            current_subset = elements[i:j + 1]
            if len(current_subset) == 793:
                subsets_count += 1
    return subsets_count