from itertools import combinations

def find_subset_of_length_n(s: set, n: int=57) -> int:
    return len(list(combinations(s, n)))