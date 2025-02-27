def find_subset_of_length_n(s):
    if len(s) < 100:
        return 0
    n = len(s)
    return (n - 99) * (n - 100) // 2