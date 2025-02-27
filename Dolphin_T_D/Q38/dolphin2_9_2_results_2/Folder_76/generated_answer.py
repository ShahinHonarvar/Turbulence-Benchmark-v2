def find_subset_of_length_n(s):
    n = len(s)
    result = 0
    for i in range(1 << n):
        subset = [s[j] for j in range(n) if i & 1 << j]
        if len(subset) == n:
            result += 1
    return result