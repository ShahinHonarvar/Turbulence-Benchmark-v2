def find_subset_of_length_n(s):
    if len(s) < 360:
        return 0
    n = len(s)
    total = 0
    for i in range(1 << n):
        subset = [s[j] for j in range(n) if i & 1 << j]
        if len(subset) == 360:
            total += 1
    return total