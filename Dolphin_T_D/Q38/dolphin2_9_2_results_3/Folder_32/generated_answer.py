def find_subset_of_length_n(s):
    if len(s) < 22:
        return 0
    n = len(s)
    p = 1
    for i in range(22, n):
        p *= i
    for i in range(n - 22, n):
        p //= i
    return p