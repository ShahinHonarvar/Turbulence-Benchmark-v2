def return_n_smallest_chars(str):
    chars = list(set(str))
    chars.sort(key=ord, reverse=False)
    return chars[:6]