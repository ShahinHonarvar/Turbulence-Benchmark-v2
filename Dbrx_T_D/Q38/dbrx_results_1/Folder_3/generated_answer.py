def find_subset_of_length_n(s):
    if len(s) < 100:
        return 0
    elif len(s) == 100:
        return 1
    else:
        return len(s) * (len(s) - 1) // 2