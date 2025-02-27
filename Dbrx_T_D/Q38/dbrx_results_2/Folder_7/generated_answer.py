def find_subset_of_length_n(s: set, n: int) -> int:
    if n < 0 or not isinstance(n, int):
        raise ValueError('n must be a non-negative integer')
    if n == 0:
        return 1
    if len(s) == 0:
        return 0
    first_elem = s.pop()
    return find_subset_of_length_n(s, n) + find_subset_of_length_n(s, n - 1)