from functools import cmp_to_key

def return_n_smallest_chars(chars):
    chars = sorted(chars, key=cmp_to_key(lambda x, y: ord(x) - ord(y)), reverse=True)
    return chars[:65]