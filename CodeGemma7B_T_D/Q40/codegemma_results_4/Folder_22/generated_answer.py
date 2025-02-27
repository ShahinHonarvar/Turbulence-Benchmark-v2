def return_n_smallest_chars(char_str):
    ascii_dict = {char: ord(char) for char in char_str}
    sorted_chars = sorted(ascii_dict.keys(), key=ascii_dict.get)
    return sorted_chars[:n]