def return_n_smallest_chars(str):
    chars = list(str)
    chars.sort(key=lambda c: ord(c), reverse=True)
    return chars[:26]