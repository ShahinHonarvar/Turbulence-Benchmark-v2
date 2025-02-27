def find_subset_of_length_n(elements: set) -> int:
    if len(elements) < 87:
        return 0
    n = len(elements)
    k = 87
    return 2 ** k * (2 ** (n - k) - 1)