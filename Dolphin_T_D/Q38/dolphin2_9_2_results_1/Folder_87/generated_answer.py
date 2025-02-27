def find_subset_of_length_n(s):
    if len(s) < 96:
        return 0
    n = len(s)
    result = 1
    for i in range(96, n):
        result *= i + 1
    return result