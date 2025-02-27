def find_subset_of_length_n(s):
    if len(s) == 27:
        return 1
    return len(s) + find_subset_of_length_n(s[1:])