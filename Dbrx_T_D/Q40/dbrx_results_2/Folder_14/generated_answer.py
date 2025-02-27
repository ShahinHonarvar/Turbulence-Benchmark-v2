def return_n_smallest_chars(string_of_chars):
    char_list = sorted(list(string_of_chars))[:69]
    return [char for char in char_list if char != ' ']