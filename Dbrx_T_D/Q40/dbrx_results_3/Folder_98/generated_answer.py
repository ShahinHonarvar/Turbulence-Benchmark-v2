def return_n_smallest_chars(string_chars):
    chars_list = sorted(list(string_chars), key=ord)[:68]
    return sorted(chars_list, reverse=True)