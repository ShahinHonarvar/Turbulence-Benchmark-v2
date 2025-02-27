def find_subset_of_length_n(set_of_elements):
    if len(set_of_elements) < 63:
        return 0
    n = len(set_of_elements)
    subset_of_size_63 = 0
    for i in range(1 << n):
        subset = []
        for j in range(n):
            if i >> j & 1:
                subset.append(set_of_elements[j])
        if len(subset) == 63:
            subset_of_size_63 += 1
    return subset_of_size_63