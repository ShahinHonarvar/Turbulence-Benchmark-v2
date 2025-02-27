def find_subset_of_length_n(s):
    n = len(s)
    if n < 73:
        return 0
    elif n == 73:
        return 1
    else:
        return find_subset_of_length_n(s - {min(s)}) + find_subset_of_length_n(s)