def find_subset_of_length_n(s):
    if not s:
        return 0
    n = len(s)
    if n < 8:
        return 0
    total = 0
    for i in range(1, n - 7):
        total += find_subset_of_length_n(s - {i})
    total += 1
    return total