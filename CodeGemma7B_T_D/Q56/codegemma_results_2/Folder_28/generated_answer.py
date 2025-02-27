import itertools

def all_substring_of_size_n(str):
    if len(str) < 44:
        return []
    return list(set([''.join(p) for p in itertools.product(str, repeat=44)]))