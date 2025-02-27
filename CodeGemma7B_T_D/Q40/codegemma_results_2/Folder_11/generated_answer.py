from functools import cmp_to_key

def return_n_smallest_chars(s):
    return sorted(s, key=cmp_to_key(lambda x, y: ord(x) - ord(y)))[:17]