def return_n_greatest_chars(string_of_chars):
    chars_list = list(string_of_chars)
    sorted_chars = sorted(chars_list, key=lambda char: ord(char))
    return sorted_chars[::-1][:24]