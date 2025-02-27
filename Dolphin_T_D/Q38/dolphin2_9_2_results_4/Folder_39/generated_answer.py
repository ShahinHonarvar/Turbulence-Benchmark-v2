def find_subset_of_length_n(s, n=59):
    if n == 0:
        return 1
    if len(s) == 0 or n > len(s):
        return 0
    return find_subset_of_length_n(s - {s[0]}, n - 1) + find_subset_of_length_n(s, n)