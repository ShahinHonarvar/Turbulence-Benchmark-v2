def return_n_smallest_chars(s):
    list = sorted(s, key=lambda c: ord(c))
    return list[:66]