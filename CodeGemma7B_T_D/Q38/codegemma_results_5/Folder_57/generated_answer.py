from itertools import combinations_with_replacement

def find_subset_of_length_n(iterable, n):
    return sum((1 for _ in combinations_with_replacement(iterable, n)))