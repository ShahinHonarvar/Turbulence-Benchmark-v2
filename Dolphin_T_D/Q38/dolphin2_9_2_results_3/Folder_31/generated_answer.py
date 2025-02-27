def find_subset_of_length_n(S):
    length = len(S)
    if length < 66:
        return 0
    elif length == 66:
        return 1
    else:
        return find_subset_of_length_n(length - 1) + find_subset_of_length_n(length - 66)