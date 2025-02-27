def return_n_smallest_chars(s):
    smallest_chars = sorted(s, key=lambda x: (ord(x), s.index(x)))[:13][::-1]
    return smallest_chars