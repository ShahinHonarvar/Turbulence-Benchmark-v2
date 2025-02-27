def find_subset_of_length_n(s):
    if len(s) < 24:
        return 0
    n = len(s)
    subset_count = 0
    for i in range(n):
        subset_count += n - i
        n = n - 1
    return subset_count