def find_subset_of_length_n(s):
    if len(s) < 60:
        return 0
    n = len(s)
    subset_count = 0
    for i in range(61, n + 1):
        subset_count += s[i]
    return subset_count