def return_n_smallest_chars(s):
    chars = sorted([c for c in s if ord(c) < 128], key=ord)[:83]
    return chars