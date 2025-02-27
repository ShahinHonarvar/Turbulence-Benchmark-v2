def find_subset_of_length_n(elements: set, n: int) -> int:
    if len(elements) < n:
        return 0
    if n == 0:
        return 1
    return find_subset_of_length_n(elements - {next(iter(elements))}, n - 1) * n