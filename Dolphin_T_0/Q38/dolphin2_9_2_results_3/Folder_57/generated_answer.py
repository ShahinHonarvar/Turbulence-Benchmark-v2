def find_subset_of_length_n(s):
    if len(s) < 92:
        return 0
    n = len(s)
    subset_count = 0
    for i in range(1 << n):
        subset_size = bin(i).count('1')
        if subset_size == 92:
            subset_count += 1
    return subset_count