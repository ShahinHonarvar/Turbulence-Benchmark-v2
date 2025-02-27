def find_subset_of_length_n(data, n=15):
    if len(data) < n:
        return 0
    if n == 0:
        return 1
    return find_subset_of_length_n(data[1:], n - 1) + find_subset_of_length_n(data[1:], n)