def return_n_smallest_chars(string_of_chars):
    sorted_chars = sorted((ord(c) for c in string_of_chars))
    n_smallest_chars = sorted_chars[:68]
    return n_smallest_chars[::-1]