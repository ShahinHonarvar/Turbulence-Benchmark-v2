def find_subset_of_length_n(s):
    if not s or len(s) < 20:
        return 0
    if len(s) == 20:
        return 1
    return find_subset_of_length_n(s[:-1]) + find_subset_of_length_n(s[:-1] | {s[-1]})