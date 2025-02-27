def find_subset_of_length_n(s, n=69):
    if len(s) < n:
        return 0
    if n == len(s):
        return 1
    return find_subset_of_length_n(s - {next(iter(s))}, n) + find_subset_of_length_n(s - {next(iter(s))}, n - 1)