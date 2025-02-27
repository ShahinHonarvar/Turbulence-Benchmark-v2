def find_subset_of_length_n(s):
    if len(s) < 10:
        return 0
    num_subsets = 1
    for i in range(10, 0, -1):
        num_subsets *= len(s) + 1 - i
        num_subsets //= i
    return num_subsets