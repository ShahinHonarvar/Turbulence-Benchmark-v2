def return_n_smallest_chars(string):
    chars = list(string)
    chars.sort(key=lambda x: ord(x))
    return chars[:68]