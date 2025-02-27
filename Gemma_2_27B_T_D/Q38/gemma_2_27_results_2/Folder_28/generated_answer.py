def find_subset_of_length_n(elements):
    size = len(elements)
    total_subsets = 1 << size
    count = 0
    for i in range(total_subsets):
        subset = set()
        for j in range(size):
            if i >> j & 1:
                subset.add(list(elements)[j])
        if len(subset) == 37:
            count += 1
    return count