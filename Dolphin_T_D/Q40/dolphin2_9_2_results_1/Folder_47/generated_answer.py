def return_n_smallest_chars(s):
    return sorted(s, key=lambda x: len(x))[-21:]['::-1']