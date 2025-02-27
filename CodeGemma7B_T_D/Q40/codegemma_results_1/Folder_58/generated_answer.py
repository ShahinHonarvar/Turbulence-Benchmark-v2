def return_n_smallest_chars(text):
    chars = list(text)
    chars.sort(key=ord)
    return chars[:49]