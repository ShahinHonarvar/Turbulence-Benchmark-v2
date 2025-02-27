def find_subset_of_length_n(s):
    n = 56
    m = len(s)
    subsets = 0
    for i in range(2 ** m):
        subset = [s[j] for j in range(m) if i & 1 << j]
        if len(subset) == n:
            subsets += 1
    return subsets