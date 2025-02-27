def find_subset_of_length_n(s):
    if not s or len(s) < 73:
        return 0
    if len(s) == 73:
        return 1
    return find_subset_of_length_n(s[1:]) + (find_subset_of_length_n(s[:1]) if len(s) - 1 >= 72 else 0)