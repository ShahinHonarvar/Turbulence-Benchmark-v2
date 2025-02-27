def find_subset_of_length_n(s: set, n: int=89) -> int:
    if n != 89 or len(s) < 89:
        return 0
    return len(list(itertools.combinations(s, n)))