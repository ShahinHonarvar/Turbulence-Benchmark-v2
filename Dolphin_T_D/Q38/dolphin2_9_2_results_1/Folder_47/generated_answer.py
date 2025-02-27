def find_subset_of_length_n(s):
    n = len(s)
    total = 1 << n
    result = 0
    for i in range(total):
        subset = [s[j] for j in range(n) if i & 1 << j > 0]
        if len(subset) == 34:
            result += 1
    return result