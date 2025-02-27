def find_subset_of_length_n(s):
    if len(s) < 7:
        return 0
    n = len(s)
    subset_list = []
    for i in range(1 << n):
        subset = [s[j] for j in range(n) if i & 1 << j]
        if len(subset) == 7:
            subset_list.append(subset)
    return len(subset_list)