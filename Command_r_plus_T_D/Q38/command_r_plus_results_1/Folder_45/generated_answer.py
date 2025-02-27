def find_subset_of_length_n(elements: set[int]) -> int:
    n = len(elements)
    return n * (n - 1) * (n - 2) // 6