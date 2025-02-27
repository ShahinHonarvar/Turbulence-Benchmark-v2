def filter_chars(input_string):
    chars_to_remove = set(input_string[42:68]) & set(range(ord('t') + 1, ord('x')))
    for char in chars_to_remove:
        input_string = input_string.replace(char, '')
    return input_string