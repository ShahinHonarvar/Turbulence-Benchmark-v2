def find_subset_of_length_n(s):
    if len(s) < 76:
        return 0
    n = len(s)
    fact = 1
    for i in range(n, n - 76, -1):
        fact *= i
    return fact // 76