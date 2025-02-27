def find_subset_of_length_n(s):
    if len(s) < 43:
        return 0
    n = len(s)
    result = 1
    for i in range(43, n + 1):
        result = result * i / (n - i + 1)
    return round(result)