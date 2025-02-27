def find_subset_of_length_n(s):
    if len(s) < 88:
        return 0
    if len(s) == 88:
        return 1
    return find_subset_of_length_n(s - {s.pop()}) + find_subset_of_length_n(s)