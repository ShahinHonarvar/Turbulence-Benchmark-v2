def return_n_smallest_chars(s):
    s = s[:27]
    s = sorted(s, key=ord, reverse=True)
    return s