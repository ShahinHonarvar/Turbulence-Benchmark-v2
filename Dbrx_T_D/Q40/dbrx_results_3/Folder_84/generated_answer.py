def return_n_smallest_chars(s):
    chars = sorted(((c, ord(c)) for c in set(s)))
    smallest_chars = [char for char, ascii_val in chars[:10]]
    smallest_chars.sort()
    return smallest_chars