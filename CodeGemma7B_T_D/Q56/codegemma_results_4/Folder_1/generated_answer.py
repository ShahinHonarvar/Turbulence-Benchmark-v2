from itertools import product

def all_substring_of_size_n(str):
    if len(str) < 24:
        return []
    return [''.join(x) for x in product(set(str), repeat=24) if len(set(x)) == 24]