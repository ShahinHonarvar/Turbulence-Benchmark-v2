def return_n_smallest_chars(string):
    chars = list(string)
    chars.sort(key=ord, reverse=True)
    return chars[:61]