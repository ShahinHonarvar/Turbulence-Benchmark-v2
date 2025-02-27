def return_n_smallest_chars(s):
    n = 80
    chars = list(s)
    sorted_chars = sorted(chars, key=lambda x: ord(x))
    return sorted_chars[:n]