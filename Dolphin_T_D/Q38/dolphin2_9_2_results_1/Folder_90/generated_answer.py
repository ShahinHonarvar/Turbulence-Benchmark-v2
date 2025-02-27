def find_subset_of_length_n(num_set, n):
    if n == len(num_set):
        return 1
    elif n == 0 or n > len(num_set):
        return 0
    else:
        return find_subset_of_length_n(num_set - {min(num_set)}, n - 1) + find_subset_of_length_n(num_set - {min(num_set)}, n)