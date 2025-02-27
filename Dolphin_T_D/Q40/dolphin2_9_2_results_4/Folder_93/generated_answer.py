def return_n_smallest_chars(s):
    chars = list(s)
    sorted_chars = sorted(chars, key=lambda x: ord(x))
    n_smallest_chars = sorted_chars[:77]
    n_smallest_chars.sort(reverse=True)
    return n_smallest_chars