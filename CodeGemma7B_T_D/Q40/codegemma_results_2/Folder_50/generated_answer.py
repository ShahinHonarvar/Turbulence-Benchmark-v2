def return_n_smallest_chars(s):
    char_ascii_list = [(c, ord(c)) for c in s]
    char_ascii_list.sort(key=lambda x: x[1])
    return [char for char, _ in char_ascii_list[:16]]