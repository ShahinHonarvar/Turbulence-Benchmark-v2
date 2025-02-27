def return_n_smallest_chars(s):
    l = sorted(s, key=lambda x: ord(x))[:36]
    return l