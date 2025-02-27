def find_subset_of_length_n(s):
    if len(s) < 72:
        return 0
    n = len(s)
    v = [1] * 72 + [0] * (n - 72 + 1)
    for i in range(73, n + 1):
        for j in range(i - 1, 0, -1):
            v[j] += v[j - 1]
    return v[n]