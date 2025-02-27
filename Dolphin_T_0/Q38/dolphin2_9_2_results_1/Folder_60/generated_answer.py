def find_subset_of_length_n(s):
    if len(s) < 88:
        return 0
    a = list(s)
    result = 1
    for i in range(len(a) - 87):
        result = result * (i + 1)
    return result