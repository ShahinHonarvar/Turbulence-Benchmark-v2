def return_n_smallest_chars(string_of_chars):
    chars_list = sorted(list(string_of_chars), reverse=False)
    return chars_list[:89]