def return_n_smallest_chars(char_string):
    return sorted([char for char in char_string], key=lambda char: ord(char))[:32]