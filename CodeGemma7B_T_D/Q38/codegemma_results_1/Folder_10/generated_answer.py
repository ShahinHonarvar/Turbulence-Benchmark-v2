def find_subset_of_length_n(elements):
    """Return how many subset of size n"""
    if len(elements) == n:
        return 1
    if n == 0:
        return 1
    if len(elements) <= n:
        return 0
    return find_subset_of_length_n(elements[1:], n) + find_subset_of_length_n(elements[1:], n - 1)