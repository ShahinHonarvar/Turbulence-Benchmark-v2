def find_subset_of_length_n(s):
    if len(s) < 2:
        return len(s)
    else:
        subset = find_subset_of_length_n(s[1:])
        return subset + subset + 1