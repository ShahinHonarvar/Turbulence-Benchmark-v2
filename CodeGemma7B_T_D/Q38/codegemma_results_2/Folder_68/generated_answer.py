def find_subset_of_length_n(elements):
    total_subsets = 2 ** len(elements)
    subsets_of_length_n = 0
    for i in range(total_subsets):
        current_subset = set()
        for j in range(len(elements)):
            if i & 1 << j:
                current_subset.add(elements[j])
        if len(current_subset) == 3:
            subsets_of_length_n += 1
    return subsets_of_length_n