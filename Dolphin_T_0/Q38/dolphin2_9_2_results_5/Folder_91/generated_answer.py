def find_subset_of_length_n(s, n):
    if n == 0:
        return 1
    if len(s) == 0:
        return 0
    return find_subset_of_length_n(s - {s[-1]}, n - 1) + find_subset_of_length_n(s - {s[-1]}, n)