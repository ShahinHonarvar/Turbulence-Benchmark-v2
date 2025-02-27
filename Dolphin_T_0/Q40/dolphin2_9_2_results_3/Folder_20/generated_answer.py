def return_n_smallest_chars(s):
    l = sorted(s, key=lambda x: ord(x))[:40]
    return l