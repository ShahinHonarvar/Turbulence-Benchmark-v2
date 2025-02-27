def find_subset_of_length_n(s):
    if len(s) < 90:
        return 0
    subset_size = 90
    subset_count = len(s) % subset_size == 0
    i = subset_size
    while i < len(s):
        subset_count += len(s) % i == 0
        i += subset_size
    return subset_count + 1