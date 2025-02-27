def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=lambda ch: ord(ch))
    return sorted_chars[:13][::-1]