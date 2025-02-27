def return_n_smallest_chars(s):
    s = sorted(s)
    return sorted(s[:48], key=lambda x: ord(x))