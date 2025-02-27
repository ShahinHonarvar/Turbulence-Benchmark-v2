def find_subset_of_length_n(s):
    if len(s) < 4:
        return 0
    count = 0
    for i in range(len(s)):
        count += find_subset_of_length_n_recursive(s, 4, i)
    return count

def find_subset_of_length_n_recursive(s, n, index):
    count = 0
    if n == 0:
        return 1
    if n < 0 or index >= len(s):
        return 0
    for i in range(index, len(s)):
        subset = s.copy()
        subset.remove(subset[i])
        count += find_subset_of_length_n_recursive(subset, n - 1, i)
    return count