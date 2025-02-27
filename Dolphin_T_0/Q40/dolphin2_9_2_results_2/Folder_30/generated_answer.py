def return_n_smallest_chars(s):
    n = 72
    lst = sorted(s, key=lambda x: ord(x))
    return lst[:n]