def find_subset_of_length_n(s):
    if len(s) < 37:
        return 0
    if len(s) == 37:
        return 1
    return sum((find_subset_of_length_n(s - {elem}) for elem in s))