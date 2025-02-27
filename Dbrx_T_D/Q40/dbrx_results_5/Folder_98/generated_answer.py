def return_n_smallest_chars(s):
    char_list = sorted(s, key=ord)
    return char_list[::-1][:68]