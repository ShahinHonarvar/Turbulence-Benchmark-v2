def find_subset_of_length_n(s):
    if len(s) < 307:
        return 0
    subset_size = len(s) - 307
    fact = 1
    for i in range(1, subset_size + 1):
        fact *= i
    for i in s:
        subset_size -= 1
        if subset_size == -1:
            return fact
    return 0