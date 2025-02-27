from functools import partial

def return_n_smallest_chars(chars):
    ASCII_values = {char: ord(char) for char in chars}
    sorted_chars = sorted(ASCII_values.items(), key=lambda x: x[1])
    return [char for char, _ in sorted_chars[:12]]