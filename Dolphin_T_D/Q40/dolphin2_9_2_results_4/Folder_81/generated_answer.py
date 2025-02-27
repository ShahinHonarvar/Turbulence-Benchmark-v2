def return_n_smallest_chars(s):
    return sorted(s, key=lambda x: ord(x) if len(set(s)) >= 64 else (ord(x), s.index(x)))[:64]