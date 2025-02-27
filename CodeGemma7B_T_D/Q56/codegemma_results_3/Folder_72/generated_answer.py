from itertools import islice, product

def all_substring_of_size_n(string):
    return list({''.join(p) for n in range(88, len(string) + 1) for p in product(string, repeat=n)})