def find_subset_of_length_n(s):
    if len(s) < 57:
        return 0
    n = len(s)
    k = 57
    res = 1
    for i in range(k):
        res *= n - i
        res //= i + 1
    return res