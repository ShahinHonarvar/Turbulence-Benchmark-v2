def find_subset_of_length_n(s):
    if len(s) < 32:
        return 0
    n = len(s)
    subset_count = 0
    for i in range(1 << n):
        subset_size = 0
        for j in range(n):
            if i >> j & 1:
                subset_size += 1
        if subset_size == 32:
            subset_count += 1
    return subset_count