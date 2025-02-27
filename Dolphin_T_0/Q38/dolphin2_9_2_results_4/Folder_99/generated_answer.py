def find_subset_of_length_n(my_set, n=307):
    length = len(my_set)
    if length < n:
        return 0
    return len(my_set) * find_subset_of_length_n(my_set - {my_set.pop()}, n - 1)