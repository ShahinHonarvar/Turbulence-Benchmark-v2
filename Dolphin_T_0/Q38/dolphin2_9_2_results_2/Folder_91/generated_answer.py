def find_subset_of_length_n(s):
    if len(s) < 6:
        return 0
    n = len(s)
    c = 1
    for i in range(6, n + 1):
        c *= i
    return c