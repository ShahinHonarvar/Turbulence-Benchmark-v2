def find_subset_of_length_n(s):
    n = len(s)
    count = 0
    for i in range(2 ** n):
        subset = [s[j] for j in range(n) if i & 1 << j]
        if len(subset) == 53:
            count += 1
    return count