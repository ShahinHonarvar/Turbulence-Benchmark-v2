def find_subset_of_length_n(s):
    length = len(s)
    if length < 84:
        return 0
    if length == 84:
        return 1
    return find_subset_of_length_n(s - 1) + find_subset_of_length_n(s // 2)