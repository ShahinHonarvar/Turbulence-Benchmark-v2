def return_n_smallest_chars(s):
    return sorted(list(s), key=lambda c: ord(c))[:7]