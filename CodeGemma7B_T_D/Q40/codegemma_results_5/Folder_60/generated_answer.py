from functools import cmp_to_key

def return_n_smallest_chars(given_str):
    return sorted(given_str, key=cmp_to_key(lambda c1, c2: ord(c1) - ord(c2)))[:28]