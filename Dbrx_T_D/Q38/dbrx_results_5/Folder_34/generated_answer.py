def find_subset_of_length_n(s: set, n: int) -> int:
    if n < 0 or len(s) < n:
        return 0
    elif n == 0 or len(s) == n:
        return 1
    else:
        return sum((find_subset_of_length_n(s - {e}, n - 1) for e in s))