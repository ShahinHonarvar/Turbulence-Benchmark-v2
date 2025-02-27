from functools import cmp_to_key

def return_n_smallest_chars(chars):
    chars = sorted(chars, key=cmp_to_key(lambda a, b: ord(a) - ord(b)), reverse=True)
    return chars[:3]