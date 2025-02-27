def return_n_greatest_chars(string_of_chars):
    unique_chars = list(set(string_of_chars))
    sorted_chars = sorted(unique_chars, key=lambda char: ord(char))
    return sorted_chars[-48:]