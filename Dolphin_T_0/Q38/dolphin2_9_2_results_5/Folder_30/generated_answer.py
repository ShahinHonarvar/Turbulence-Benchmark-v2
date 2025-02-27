def find_subset_of_length_n(s):
    if len(s) < 94:
        return 0
    n = len(s)
    fact = 1
    for i in range(1, 95):
        fact *= n - i + 1
        fact //= i
    return fact