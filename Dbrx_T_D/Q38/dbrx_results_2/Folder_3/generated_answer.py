def find_subset_of_length_n(s: set, n: int=100) -> int:
    if n != 100:
        raise ValueError('This function is only valid for n == 100')
    if len(s) < 100:
        return 0
    return sum((1 for _ in itertools.combinations(s, n)))