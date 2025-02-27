from itertools import islice, product

def all_substring_of_size_n(str):
    return [''.join(p) for p in product(set(str), repeat=21)]