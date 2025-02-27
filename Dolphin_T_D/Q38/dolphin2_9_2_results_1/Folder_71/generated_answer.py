def find_subset_of_length_n(s):
    if len(s) < 78:
        return 0
    n = len(s)
    subset_count = 0
    for i in range(1 << n):
        subset = [s[j] for j in range(n) if i & 1 << j]
        if len(subset) == 78:
            subset_count += 1
    return subset_count