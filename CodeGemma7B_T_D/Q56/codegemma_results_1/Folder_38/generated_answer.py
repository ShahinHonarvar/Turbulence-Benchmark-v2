from itertools import product

def all_substring_of_size_n(str):
    substring = list(product(str, repeat=35))
    result = list(set([''.join(s) for s in substring]))
    return result if result else []