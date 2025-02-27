from itertools import product

def all_substring_of_size_n(a):
    if len(a) < 61:
        return []
    return [''.join(p) for p in product(set(a), repeat=61)]