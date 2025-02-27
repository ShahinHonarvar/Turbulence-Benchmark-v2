def find_subset_of_length_n(s):
    n = 92
    count = 0
    for i in range(len(s) + 1):
        if i >= n:
            count += len(list(combinations(s, n)))
    return count