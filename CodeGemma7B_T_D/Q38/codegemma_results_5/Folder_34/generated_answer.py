def find_subset_of_length_n(set):
    len_set = len(set)
    bin_mask = (1 << len_set) - 1
    count = 0
    for mask in range(bin_mask + 1):
        subset = set()
        for i in range(len_set):
            if mask & 1 << i != 0:
                subset.add(set[i])
        if len(subset) == 97:
            count += 1
    return count