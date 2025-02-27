def return_n_smallest_chars(str):
    chars = list(set(str))
    chars.sort(key=ord, reverse=True)
    return chars[:68]