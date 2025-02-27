def find_subset_of_length_n(s):
    if len(s) < 37:
        return 0
    count = len(s)
    length = 37
    for i in range(length, 0, -1):
        count *= count - i
    return count