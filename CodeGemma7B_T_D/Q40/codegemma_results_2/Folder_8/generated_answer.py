def return_n_smallest_chars(chars):
    ascii_values = sorted([ord(c) for c in chars], key=ord)
    return [chr(value) for value in ascii_values[:83]]