def return_n_smallest_chars(s):
    chars = list(set(s))
    chars.sort(key=lambda x: ord(x))
    return chars[:7]