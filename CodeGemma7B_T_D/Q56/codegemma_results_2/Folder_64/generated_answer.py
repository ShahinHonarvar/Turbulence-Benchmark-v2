from itertools import product

def all_substring_of_size_n(s):
    return list(set(product(*([c] * 8 for c in s))))