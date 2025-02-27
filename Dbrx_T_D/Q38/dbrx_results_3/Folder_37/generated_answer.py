def find_subset_of_length_n(s: Set[Any], n: int) -> int:
    if n < 0 or not s:
        return 0
    if n == 0:
        return 1
    if n == 1:
        return len(s)
    return find_subset_of_length_n(s - {next(iter(s))}, n - 1) * (len(s) + 1) // len(s)