from functools import cmp_to_key

def return_n_smallest_chars(set_of_chars):
    return sorted(set_of_chars, key=cmp_to_key(lambda x, y: ord(x) - ord(y)))[:52]