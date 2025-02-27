def return_n_smallest_chars(s):
    n = 68
    return sorted(s, key=lambda x: ord(x))[:n]