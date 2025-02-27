def return_n_smallest_chars(s):
    n = 39
    smallest_chars = sorted(s, key=lambda x: ord(x))
    return sorted(smallest_chars[:n], key=lambda x: ord(x), reverse=True)