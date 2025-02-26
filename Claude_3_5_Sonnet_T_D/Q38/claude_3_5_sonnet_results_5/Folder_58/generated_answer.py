def find_subset_of_length_n(elements):
    n = len(elements)
    k = 860
    if k > n:
        return 0
    result = 1
    for i in range(k):
        result *= n - i
        result //= i + 1
    return result