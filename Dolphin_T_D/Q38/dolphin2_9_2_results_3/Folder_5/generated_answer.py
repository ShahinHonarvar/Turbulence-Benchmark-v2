def find_subset_of_length_n(s):
    n = 67
    if len(s) < n:
        return 0
    subset_count = 0
    for i in range(len(s)):
        if s[i] > n:
            subset_count += find_subset_of_length_n(s[i + 1:])
        else:
            subset_count += 1
    return subset_count