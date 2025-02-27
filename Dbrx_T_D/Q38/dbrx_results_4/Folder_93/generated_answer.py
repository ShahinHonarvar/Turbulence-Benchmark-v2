import math

def find_subset_of_length_n(s, n):
    if n == 0:
        return {frozenset()}
    if not s:
        return set()
    x = s.copy()
    x.remove(s.pop())
    return {y | {s} for s in x if len((y := find_subset_of_length_n(x, n - 1))) > 0}

def count_subsets_of_size_N(s, N):
    return sum((1 for _ in find_subset_of_length_n(s, N)))