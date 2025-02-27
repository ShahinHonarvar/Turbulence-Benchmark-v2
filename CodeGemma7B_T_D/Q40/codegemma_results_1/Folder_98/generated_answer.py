def return_n_smallest_chars(string):
    """Return the smallest characters in the given string"""
    char_list = sorted(list(string), key=ord)[:68]
    return char_list[::-1]