def find_subset_of_length_n(elements: set) -> int:
    n = len(elements)
    if n < 7:
        return 0
    else:
        return (n - 1) * (n - 2) * (n - 3) * (n - 4) * (n - 5) * (n - 6) // (7 * 6 * 5 * 4 * 3 * 2)