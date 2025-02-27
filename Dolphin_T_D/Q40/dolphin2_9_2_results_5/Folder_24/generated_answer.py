def return_n_smallest_chars(s):
    s = list(s)
    s.sort(key=lambda x: ord(x))
    return s[:32]