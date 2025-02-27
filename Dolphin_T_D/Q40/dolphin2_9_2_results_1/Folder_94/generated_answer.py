def return_n_smallest_chars(chars):
    n = 87
    chars = list(chars)
    chars.sort(key=lambda x: ord(x))
    return chars[::-1][:n]