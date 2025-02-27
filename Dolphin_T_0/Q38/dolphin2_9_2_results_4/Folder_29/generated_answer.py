def find_subset_of_length_n(s):
    if len(s) < 19:
        return 0
    subset_count = 0
    for i in range(len(s)):
        subset_count += find_subset_of_length_n_helper(s, i + 1, 19)
    return subset_count

def find_subset_of_length_n_helper(s, n, m):
    if m == 0 or n == 0:
        return 1
    if n < 0 or m < 0:
        return 0
    return find_subset_of_length_n_helper(s, n - 1, m) + find_subset_of_length_n_helper(s, n - 1, m - 1)