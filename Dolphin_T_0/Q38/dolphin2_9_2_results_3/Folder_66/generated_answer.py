def find_subset_of_length_n(s):
    if type(s) != set:
        s = set(s)
    x = len(s)
    if x >= 42:
        return 2 ** 42
    return 0