def return_n_smallest_chars(input_string):
    ascii_dict = {char: ord(char) for char in input_string}
    sorted_chars = sorted(ascii_dict.keys(), key=ascii_dict.get)
    return sorted_chars[:32]