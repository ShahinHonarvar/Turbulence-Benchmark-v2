def find_subset_of_length_n(elements):
    total_subsets = 2 ** len(elements)
    subsets_of_length_n = 0
    for i in range(total_subsets):
        subset = set()
        for j, element in enumerate(elements):
            if i >> j & 1:
                subset.add(element)
        if len(subset) == 69:
            subsets_of_length_n += 1
    return subsets_of_length_n