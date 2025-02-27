def find_subset_of_length_n(s, n=14):
    if not isinstance(s, set) or not isinstance(n, int) or n < 0:
        raise ValueError('Invalid input. The first argument must be a set and the second argument must be a non-negative integer.')
    if not s:
        return 0 if n else 1
    elem = list(s)[0]
    remaining = s - {elem}
    with_elem = find_subset_of_length_n(remaining, n - 1) * (len(s) - 1)
    without_elem = find_subset_of_length_n(remaining, n)
    return with_elem + without_elem